#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def my_del(delt):
        return (delt if delt != search else replace)
    return list(map(my_del, my_list))
