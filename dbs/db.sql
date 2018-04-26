/*
Navicat MySQL Data Transfer

Source Server         : MyWeb
Source Server Version : 50719
Source Host           : localhost:3306
Source Database       : nahsor

Target Server Type    : MYSQL
Target Server Version : 50719
File Encoding         : 65001

Date: 2018-04-19 11:31:53
*/

SET FOREIGN_KEY_CHECKS=0;


DROP DATABASE IF EXISTS nahsor;
CREATE DATABASE nahsor DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_general_ci;


USE nahsor;


-- ----------------------------
-- Table structure for t_testcass
-- ----------------------------
DROP TABLE IF EXISTS `t_testcass`;
CREATE TABLE `t_testcass` (
  `id` int(16) NOT NULL AUTO_INCREMENT,
  `cassname` varchar(255) NOT NULL COMMENT '用例名称',
  `testcass` json NOT NULL COMMENT '用例内容，以json格式储存',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatatime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




INSERT INTO `nahsor`.`t_testcass` (`id`, `cassname`, `testcass`, `remark`, `createtime`, `updatatime`) VALUES ('1', 'tastcass', '{\"req\": {\"url\": \"http://127.0.0.1:2333/test\", \"json\": {\"aaa\": \"bbb\"}, \"method\": \"GET\", \"headers\": {\"Content-Type\": \"application/json\"}, \"timeout\": 10}, \"cass_name\": \"test_name\", \"validates\": [{\"Equal\": [\"r.json()\", \"self.req[\\\"json\\\"]\"]}, {\"Equal\": [\"r.status_code\", \"200\"]}]}', '2333', '2018-04-19 14:48:25', '2018-04-24 18:46:12');
INSERT INTO `nahsor`.`t_testcass` (`id`, `cassname`, `testcass`, `remark`, `createtime`, `updatatime`) VALUES ('2', 'tastcass', '{\"req\": {\"url\": \"http://127.0.0.1:2333/test\", \"json\": {\"aaa\": \"bbb\"}, \"method\": \"GET\", \"headers\": {\"Content-Type\": \"application/json\"}, \"timeout\": 10}, \"cass_name\": \"test_name111\", \"validates\": [{\"Equal\": [\"r.json()\", \"self.req[\\\"json\\\"]\"]}, {\"Equal\": [\"r.status_code\", \"201\"]}]}', '2333', '2018-04-19 14:48:31', '2018-04-24 18:46:30');
