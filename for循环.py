
def aa():
    a = [11, 22, 33, 44]
    b = [66, 77, 88, 99]
    c=[1,2,3]
    item = []
    for i in a:

        item.append(i)
    for j in b:
        item.append(j)
        for j in c:
            item.append(j)
    print(item)

# str= "https://list.suning.com/1-502679-2-0-0-0-0-14-0-4.html"
# str1 = 'https://list.suning.com/1-502680-0.html'
# next_part_url = 'https://list.suning.com/emall/showProductList.do?ci={}&pg=03&cp={}&il=0&iy=-1&adNumber=0&n=1&ch=4&prune=0&sesab=ACBAAB&id=IDENTIFYING&cc=010&paging=1&sub=0'
# ci = str1.split("-")[1]
# cp= str1.split("-")[2]
# cp= cp.split(".")[0]
# next_part_url = next_part_url.format(ci,cp)
# print(next_part_url)

# https://list.suning.com/1-502688-0.html
# https://list.suning.com/1-502688-0-0-0-0-0-14-0-4.html
# item["title_2"] = li.xpath("./a/text()").extract_first()

# uu1 = 'https://list.suning.com/1-502688-0.html'
# print(str(uu1).rsplit('.',1)[0])
# print(str(uu1).rsplit('.',1)[0])
# # uu = str(uu1.rsplit('.',1)[0]) + "-0-0-0-0-14-0-4.html"
# # print(uu)

uu1 = 'https://list.suning.com/1-502688-3-0-0-0-0-14-0-4.html'
print(str(uu1).split('-')[1])
print(str(uu1).split('-')[2])
# next = "/1-502687-65-0-0-0-0-14-0-4.html"
# next_url = "https://list.suning.com"+next
# print(next_url)
# current_page_num = '2'
# next_url = 'https://list.suning.com/1-502687-{}-0-0-0-0-14-0-4.html'.format(current_page_num)
# print(next_url)