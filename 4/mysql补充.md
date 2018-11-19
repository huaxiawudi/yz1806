## 一、索引

索引就像图书的目录，可以加快查询速度

### 1.1 索引的优点

- 可以大大加快数据的检索速度
- 唯一索引可以保证数据的唯一性
- 可以降低分组、排序的时间
- 可以使用查询优化器提高系统性能

### 1.2 索引的缺点

- 建立索引会建立对应索引文件，占用大量空间
- 建立索引会降低增、删、改的效率

### 1.3 不建立索引

- 频繁更新的字段不要建立索引
- 没出现在where、having，不要建立索引
- 数据量少的表没有必要建立索引
- 唯一性比较差的字段不要建立索引

### 1.4 索引分类

#### 普通索引

```
create index 索引名 on 表名(字段 asc/desc) 默认asc升序
```

#### 唯一索引

  在唯一索引所在列不能有重复值，增加和修改会受影响。

```
create  unique index 索引名 on 表名(字段 asc/desc) 默认asc升序
```

#### 主键索引

  创建表，主键索引会自动添加，要求在主键上不能有重复值，不能有空值

#### 复合索引（联合索引） 索引了多个列

- 使用联合索引，必须包含左前缀。  （a,b,c)
  - a
  - a,b
  - a,b,c

#### 全文索引（了解）

   一般会用全文索引服务器(sphinx)，不会直接创建全文索引

```
create  FULLTEXT index 索引名 on 表名(字段 asc/desc)
```

#### 删除索引

```
drop index 索引名 on 表
```

#### 查看索引

```
show index from 表 \G

#查看sql性能
explain select sno,sname from student where class='1812'\G;
mysql> explain select sno,sname from student where sclass='1812' ;
+----+-------------+---------+------------+------+---------------+------+---------+------+------+----------+-------------+
| id | select_type | table   | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
+----+-------------+---------+------------+------+---------------+------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | student | NULL       | ALL  | NULL          | NULL | NULL    | NULL |   10 |    10.00 | Using where |
+----+-------------+---------+------------+------+---------------+------+---------+------+------+----------+-------------+
1 row in set, 1 warning (0.00 sec)
type:  ALL  全表扫描
       index  使用索引
       range  在指定范围内使用索引
       const、system 常量查询

```

#### 其它创建索引的方式

```
alter table 表 add index(字段1,字段2,...)
alter table 表 add primary key(字段1,字段2,...)
alter table 表 add unique(字段1,字段2,...)
alter table 表 add fulltext(字段1,字段2,...)
```

### 1.5 不使用索引的情况

- 查询时的联合索引没有左前缀，不使用索引
- or条件里，如果一方字段没有索引，则不使用索引
- 类型不对应的不会使用索引
- like  '%tom' ,如果左边是通配符，不会使用索引
- 使用!=、<>、not in操作，不使用索引



## 二、外键

如果表A的主关键字是表B中的字段，则该字段称为表B的外键，表A称为主表，表B称为从表

- 数据表引擎必须是innodb
- 主表和从表相关的外键字段类型必须兼容

```
创建外键
ALTER TABLE 从表名
ADD CONSTRAINT 外键名称 FOREIGN KEY (从表的外键列) REFERENCES 主表名 (主键列) 
[ON DELETE reference_option]
[ON UPDATE reference_option]

reference_option:
RESTRICT | CASCADE | SET NULL | NO ACTION
  1. CASCADE: 从父表中删除或更新对应的行，同时自动的删除或更新子表中匹配的行。ON DELETE CANSCADE和ON UPDATE CANSCADE都被InnoDB所支持。
  
  2. SET NULL: 从父表中删除或更新对应的行，同时将子表中的外键列设为空。注意，这些在外键列没有被设为NOT NULL时才有效。ON DELETE SET NULL和ON UPDATE SET SET NULL都被InnoDB所支持。

  3. NO ACTION: InnoDB拒绝删除或者更新父表。

  4. RESTRICT: 拒绝删除或者更新父表。指定RESTRICT（或者NO ACTION）和忽略ON DELETE或者ON UPDATE选项的效果是一样的。

删除外键
ALTER TABLE 从表 DROP FOREIGN KEY 外键名
```

