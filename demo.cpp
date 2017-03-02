#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
/*
struct func{
    unsigned int offset;
    unsigned int length;
    func(int _offset,int _length):offset(_offset),length(_length){}
    func(func& _func){
        offset = _func.offset;
        length = _func.length;
    }
    void print(){
        std::cout<<offset<<" "<<length<<std::endl;
    }
};
*/
struct entry{
    unsigned int in_offset,in_length,out_offset,out_length;
    //entry(func& _in,func& _out):in(_in),out(_out){}
    //entry(entry& _entry):in(_entry.in),out(_entry.out){}
    entry(int _in_offset,int _in_length,int _out_offset,int _out_length):
        in_offset(_in_offset),in_length(_in_length),out_offset(_out_offset),out_length(_out_length)
        {}
    void print(){
        std::cout<<in_offset<<" "<<in_length<<" "<<out_offset<<" "<<out_length<<std::endl;
    }
};
using namespace std;
int main(){
    fstream in("codeinfo.txt");
    map<string,vector<entry> > cls;
    int num,func_num;
    in>>num;
    int tmp_in_offset,tmp_in_length,tmp_out_offset,tmp_out_length;
    string cls_name;
    for(int cls_index = 0;cls_index!=num;++cls_index){
       in>>cls_name>>func_num;
       for(int i=0;i!=func_num;++i){
           in>>tmp_in_offset>>tmp_in_length>>tmp_out_offset>>tmp_out_length;
           //func input(tmp_in_offset,tmp_in_length),out(tmp_out_offset,tmp_out_length);
           entry ent(tmp_in_offset,tmp_in_length,tmp_out_offset,tmp_out_length);
           cls[cls_name].push_back(ent);
       }
    }
    for(map<string,vector<entry> >::iterator it=cls.begin();it!=cls.end();++it){
        cout<<it->first<<endl;
        for(int i=0;i!=it->second.size();++i){
            it->second[i].print();
        }
    }
    return 0;
}
