
# bytes_a = b'\xe6\x89\x8e\xe5\xbf\x83\xe4\xba\x86\xef\xbc\x8c\xe8\x80\x81\xe9\x93\x81'
# print(type(bytes_a))
# print(bytes_a.decode("utf-8", "strict"))


# clean nums in listitem

def cleannums_list(lst):
    return_list = []
    for item in lst:
        for c in  item:
            if c.isalpha() != True:
                item = item.replace(c,"")
        return_list.append(item)
    return return_list


raw_list = ['123adf213','456dfgas','234zxs34','34s3245sa','234aedf']
clean_list = cleannums_list(raw_list)
output_list = zip(range(1,len(clean_list)+1),clean_list)
for k,v in output_list:
    print(k,v)
print(clean_list)
print(list(map(lambda x:x*2,clean_list)))
print(list(map(lambda word:word.upper(),clean_list)))
print(list(enumerate(clean_list)))
print(list(reversed(clean_list)))
print(sorted(clean_list))
clean_list.extend('extend')
print(clean_list)
clean_list.append('append')
print(clean_list)


s = 'abcdefg'

print(s.copy(2))