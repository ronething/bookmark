
#coding=utf-8

import json

input_file = '../Bookmarks'
out_file = '../bookmark.json'

# 最终存储 json 数据 data:[] list 的元素为 {"name":"xx","url":"xx"}
out_list = []

def json_for_node(node):
    if 'url' in node:
        yield dict(name=node['name'],url=node['url'])
    elif 'children' in node:
        for n in node['children']:
            yield json_for_node(n)
    else:
        yield 'nothing'

def export_json(node):
    if 'url' in node:
        out_list.append(dict(name=node['name'],url=node['url']))
    elif 'children' in node:
        for n in node['children']:
            export_json(n)
    else:
        return 'nothing'

def yield_main():
    with open(input_file,'r',encoding='utf-8') as f:
        contents = json.loads(f.read())
    
    # bookmark_bar =  json_for_node(contents['roots']['bookmark_bar'])
    other = json_for_node(contents['roots']['other'])
    while True:
        try:
            out_list.append(next(next(other)))
        except StopIteration:
            print(out_list)
            break

def main():
    with open(input_file,'r',encoding='utf-8') as f:
        contents = json.loads(f.read())
    
    bookmark_bar =  export_json(contents['roots']['bookmark_bar'])
    other = export_json(contents['roots']['other'])
    out_json = dict(data=out_list)
    with open(out_file,'w+',encoding='utf-8') as f:
        f.write(json.dumps(out_json,ensure_ascii=False))

if __name__ == "__main__":
    main()


