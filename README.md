# chrome bookmark 整理分析

## 0x00

首先读取 bookmark 不同操作系统的 bookmark 在不同的路径

## 0x01

```sh
In [35]: contents.keys()                                                      
Out[35]: dict_keys(['checksum', 'roots', 'version'])
```

checksum 和 version 我们不关心

重点在 roots 里面存放着 chrome 浏览器的所有书签

```sh
In [37]: contents['roots'].keys()                                             
Out[37]: dict_keys(['bookmark_bar', 'other', 'sync_transaction_version', 'synced'])
```

其中 bookmark_bar 和 other 分别表示书签栏和其他书签 属于同级事物

```sh
In [40]: contents['roots']['bookmark_bar']['name']                            
Out[40]: '书签栏'

In [41]: contents['roots']['other']['name']                                   
Out[41]: '其他书签'

In [42]: contents['roots']['bookmark_bar'].keys()                             
Out[42]: dict_keys(['children', 'date_added', 'date_modified', 'id', 'name', 'sync_transaction_version', 'type'])

In [43]: contents['roots']['other'].keys()                                    
Out[43]: dict_keys(['children', 'date_added', 'date_modified', 'id', 'name', 'sync_transaction_version', 'type'])
```

其中，children 下面是一个 list 而 list 中的每个元素其实是一个 dict 表示具体书签项目

每个具体的书签项目拥有的 key

```sh
date_added
id
meta_info
name
sync_transaction_version
type
url
```

