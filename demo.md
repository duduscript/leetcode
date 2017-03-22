---
title : 《OAuth Demystified for Mobile Application Developers》阅读笔记
date : 2017-03-21
tags : security
categories : lab

---

# OAuth Demystified for Mobile Application Developers

如果对OAuth协议不了解，先看协议的RFC了解一些。


## OAUTH的背景

OAuth协议最开始是为网站提供一种安全授权机制，它定义了一套用户授权给第三方应用获取用户在资源提供方上的流程。OAuth协议在工业界广泛使用以后，很多公司将其重新应用于认证。

<!-- more -->

OAuth1.0是最早的OAuth版本，另一个广泛应用于第三方用户认证的是OpenID，OAuth协议设计的主要为了解决OpenID没有解决的问题---授权，OAuth协议本身并没有要用于认证。

### OAuth1.0和OAuth1.0a

OAuth1.0协议流程如Figure 1 所示，所有的虚线表示浏览器重定向，实线表示server-to-server API调用。


### OAuth2.0

OAuth2.0不是对OAuth1.0的修改，而是完全重新设计了一个新的协议。论文主要讲了4个流程中的两个，implicit grant 和authorization code 如图 Figure2a 和 Figure2b所示

#### Implicit grant

有两个优点，第一,所有的消息由User Agent来交换(重定向);第二，不需要依赖方提供 shared secure给资源提供方。

我的看法是，implicit grant流程的好处是显而易见的，就是十分简单，因为不需要第三方应用服务器与资源提供方通信，所以第三方应用使用不再需要额外的服务器代码。这个对于移动平台来说是非常适合的，但这个流程不能用来认证，这个再接下来会描述。

#### Authorization code

额外的认证了依赖方，流程细节见RFC

## Our Study

主要是两个方面:

* 理解和比较OAuth1.0和2.0，找到用于认证和授权的关键步骤。这些步骤在移动端实现的机制和web端很不一样
* 通过对149款受欢迎的移动应用的研究，理解现实中的开发者对协议的解释和实现

## OAuth Specification and Mobile Platforms

### Dissecting the OAuth specification

分析集中在授权与认证，上述的OAuth1.0与OAuth2.0，以及OAuth1.0的流程和OAuth2.0的两张流程.值得注意的是,OAuth协议流程的前提条件是依赖方必须得到一个ID和与资源提供方的shared secure，这个通常是依赖方应用最开始向资源提供方注册的。

#### Authorization

the Security audience是资源提供方，资源提供方必须确认资源送到了用户授权的地方。

#### Authentication

很多网站和应用用OAuth来做认证，但实际上标准协议中并没有描述用于认证，认证中的security audience是依赖方。

总的来说，为了决定是否可以认证，要确定两点：

* 依赖方必须确认从资源提供方传递的user ID不能被篡改

* 依赖方必须检查OAuth tokens是否给了同一个依赖方

OAuth2.0 implicit grant 对于认证是不安全的，access tokens并没有和依赖方绑定，所以无法确认是否登录同一个依赖方。

### 移动端和web端在OAuth 安全方面的不同

#### 不同的重定向机制

在OAuth协议中用得非常多的一个web概念是重定向，用来将用户定向到服务提供方并且传递OAuth tokens给依赖方。重定向过程中，浏览器对于HTTP302状态码的定义非常清楚，但是在移动端却不是那么清晰，FRC中的说明也不是很清楚。

在移动平台上边和重定向最接近的一个概念是IOS的custom scheme机制，以及Android的Intent机制。它们被应用用来在移动端注册自己的custom URI schemes。当移动端浏览器访问custom scheme的URI，OS会启动注册这个URI的应用。但是和DNS协议不一样，再系统中多个应用可以注册同一个URI，这中多对一的映射是一种基本的缺陷。


#### 应用身份

另一个问题是不能确认接受者的身份信息，在传统的web端有DNS负责，但在移动端包括IOS和ANdroid都没有相同的概念。因为下载的应用都没有一个关联的和它们关联的origin，很难保证资源提供方的confidential message传到了期望的接受者。

### 客户端协议逻辑

像Intent这种客户端的消息传输机制通常用来代替浏览器的重定向，但浏览器重定向和客户端信息传输机制有很大的区别。当用客户端消息传输机制时(Android Intent)，传输的信息需要现在移动端处理。理论上所有的核心逻辑应该放在服务器而不是移动端，移动端只需要向服务器收发信息，但这个很难做到。根据研究，很多移动开发者错误的把应用的核心逻辑放在了移动端。

## real-world 移动应用研究

研究的重点是开发者是怎么处理一些协议中的重要部分，并是否注意到平台的不同的问题。

### Storing relying party secrets locally

一个常见的问题是很多开发者错误理解依赖方secret，并把它存在客户端应用中。OAuth中有误导开发者的点，OAuth1.0中把它叫做"consumer secret"，OAuth2.0中把它叫做"client secret"，这个名字对于没有看协议描述的人有很大误导。

Pinterest和Quora都存在这个问题，在用Twitter作为资源提供方授权的时候。都将"secret"放在了应用。更严重的是web端用的"secret"也是一样的。

### Using authorization flows for authentication

另一个常见问题是把认证和授权当做同一个问题，我们以Facebook的依赖方作为研究。

Facebook将implicit grant进行了改进，加入了appsecret_proof字段。但大多数应用没有使用改进的协议，84.7%的依赖方用的是常规的implicit grant，另外还有一个应用错误地实现了这个协议。

### 在移动应用中处理重定向

#### Custom scheme and Intent

根据Apple，如果IOS应用试图注册同一个custom scheme，关于哪个APP相关是未定义行为。对于IOS，没有服务提供者正确使用了custom scheme，因为没有服务提供者能够确认接受者的身份。在Android端中，服务提供者可以安全使用Intent机制，Android端可以通过Android key hash验证接受者的身份。当依赖方应用向服务提供方注册的时候，需要用依赖方的Android developer key的hash。

#### Mobile brower and WebView

OAuth协议在移动端依赖方和基于web服务提供方之间很难实现，因为服务提供方很难确认移动端身份。我们研究中注意到了两个有缺陷的方式：

** 用custom scheme和custom Intent filters **

将OAuth tokens传递给移动端依赖方是将依赖方的custom scheme，IOS上的custom scheme是不安全的。Android端的验证hash key的方式只是针对native应用。基于web的服务提供方在浏览器内部无法验证。

** 用URI参数 **

另一种方式是在资源提供方URI后边加参数来重定向，如果依赖方应用在WebView中访问资源提供方，然后依赖方可以通过getURI()函数API来得到参数。但这种方式问题在于服务提供方不能确定host应用的身份。


### Inventing home-brewed protocol flows

有的服务提供方提供了自家的"OAuth-based"协议流程，比如腾讯。











