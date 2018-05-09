/*
Navicat MySQL Data Transfer

Source Server         : MyWeb
Source Server Version : 50719
Source Host           : localhost:3306
Source Database       : nahsor

Target Server Type    : MYSQL
Target Server Version : 50719
File Encoding         : 65001

Date: 2018-05-09 19:12:46
*/

DROP DATABASE IF EXISTS nahsor;
CREATE DATABASE nahsor DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_general_ci;

USE nahsor;
-- ----------------------------
-- Table structure for t_config
-- ----------------------------
DROP TABLE IF EXISTS `t_config`;
CREATE TABLE `t_config` (
  `id` int(11) NOT NULL,
  `url` json DEFAULT NULL,
  `headers` json DEFAULT NULL,
  `method` json DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of t_config
-- ----------------------------
INSERT INTO `t_config` VALUES ('1', '[\"www.baidu.com\"]', '{\"content-type\": \"application/json\"}', '[\"POST\", \"GET\"]');

-- ----------------------------
-- Table structure for t_modules
-- ----------------------------
DROP TABLE IF EXISTS `t_modules`;
CREATE TABLE `t_modules` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `projectid` int(16) NOT NULL COMMENT '所属项目id',
  `modules` varchar(255) NOT NULL COMMENT '模块名称',
  `explain` varchar(255) DEFAULT NULL COMMENT '描述',
  `leader` varchar(255) DEFAULT NULL COMMENT '负责人',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatatime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `modules` (`modules`),
  KEY `project` (`projectid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of t_modules
-- ----------------------------
INSERT INTO `t_modules` VALUES ('1', '1', '测试模块', '描述', '责任人', '备注', '2018-05-03 14:55:01', '2018-05-03 14:55:01');
INSERT INTO `t_modules` VALUES ('2', '1', '测试模块', '描述', '责任人', '备注', '2018-05-03 14:55:08', '2018-05-03 14:55:08');
INSERT INTO `t_modules` VALUES ('3', '1', '测试模块', '描述', '责任人', '备注', '2018-05-03 14:55:09', '2018-05-03 14:55:09');
INSERT INTO `t_modules` VALUES ('4', '1', '测试模块', '描述', '责任人', '备注', '2018-05-03 14:55:16', '2018-05-03 14:55:16');

-- ----------------------------
-- Table structure for t_product
-- ----------------------------
DROP TABLE IF EXISTS `t_product`;
CREATE TABLE `t_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `product` varchar(64) NOT NULL COMMENT '产品名称',
  `explain` varchar(255) DEFAULT NULL COMMENT '负责人',
  `leader` varchar(16) DEFAULT NULL COMMENT '状态，0可用，1不可用',
  `remark` varchar(255) DEFAULT NULL COMMENT '说明，描述',
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatatime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `product` (`product`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of t_product
-- ----------------------------
INSERT INTO `t_product` VALUES ('1', '测试产品1', '描述', '责任人', '备注', '2018-05-03 13:11:04', '2018-05-03 13:11:04');
INSERT INTO `t_product` VALUES ('2', '产品名称22', '描述1112', '责任人2', '备注1', '2018-05-06 04:26:20', '2018-05-06 04:26:20');

-- ----------------------------
-- Table structure for t_project
-- ----------------------------
DROP TABLE IF EXISTS `t_project`;
CREATE TABLE `t_project` (
  `id` int(16) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `productid` int(16) NOT NULL COMMENT '关联的产品id',
  `project` varchar(255) NOT NULL COMMENT '项目名称',
  `explain` varchar(255) DEFAULT NULL COMMENT '描述',
  `leader` varchar(255) DEFAULT NULL COMMENT '负责人',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatatime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `project` (`project`),
  KEY `product` (`productid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of t_project
-- ----------------------------
INSERT INTO `t_project` VALUES ('1', '2', '项目名称1', '描述', '负责人', '备注', '2018-05-03 13:59:35', '2018-05-03 13:59:35');
INSERT INTO `t_project` VALUES ('2', '2', '项目名称2', '描述', '负责人', '备注', '2018-05-03 13:59:36', '2018-05-03 13:59:36');
INSERT INTO `t_project` VALUES ('3', '1', '项目名称3', '描述', '负责人', '备注', '2018-05-03 13:59:42', '2018-05-03 13:59:42');

-- ----------------------------
-- Table structure for t_testcass
-- ----------------------------
DROP TABLE IF EXISTS `t_testcass`;
CREATE TABLE `t_testcass` (
  `id` int(16) NOT NULL AUTO_INCREMENT,
  `moduleid` int(16) NOT NULL COMMENT '所属模块id',
  `testname` varchar(32) NOT NULL COMMENT '用例名称',
  `testtype` varchar(16) DEFAULT NULL COMMENT '用例类型',
  `explain` varchar(255) DEFAULT NULL COMMENT '用例描述',
  `status` int(16) DEFAULT '0' COMMENT '执行状态，0：未执行   1：成功    2：失败',
  `request` json NOT NULL COMMENT '请求参数',
  `validate` json DEFAULT NULL COMMENT '校验参数',
  `extract` json DEFAULT NULL COMMENT '提取参数',
  `leader` varchar(255) DEFAULT NULL COMMENT '负责人',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatatime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_testcass
-- ----------------------------
INSERT INTO `t_testcass` VALUES ('1', '1', 'tastcass1', 'testcass', '2333', '0', '{\"url\": \"http://127.0.0.1:2333/tes1t\", \"json\": {\"aaa\": \"bbb\"}, \"method\": \"POST\", \"headers\": {\"Content-Type\": \"application/json\"}, \"timeout\": 10}', '[{\"Equal\": [\"r.json()\", \"request[\\\"json\\\"]\"]}, {\"Equal\": [\"r.status_code\", \"200\"]}]', '{}', 'Jin', '2333', '2018-05-09 18:15:51', '2018-05-09 18:15:51');
INSERT INTO `t_testcass` VALUES ('2', '1', 'tastcass2', 'testcass', '2333', '0', '{\"url\": \"http://127.0.0.1:2333/test\", \"json\": {\"aaa\": \"bbb\"}, \"method\": \"POST\", \"headers\": {\"Content-Type\": \"application/json\"}, \"timeout\": 10}', '[{\"Equal\": [\"r.json()\", \"request[\\\"json\\\"]\"]}, {\"Equal\": [\"r.status_code\", \"201\"]}]', '{}', 'Jin', '2333', '2018-05-09 18:15:55', '2018-05-09 18:15:55');
INSERT INTO `t_testcass` VALUES ('3', '1', '测试流程', 'testsuite', '2333', '0', '{\"url\": \"http://127.0.0.1:2333/login\", \"json\": {\"password\": \"123456\", \"username\": \"admin\"}, \"method\": \"POST\", \"headers\": {\"Content-Type\": \"application/json\"}, \"timeout\": 10}', '[{\"Equal\": [\"r.status_code\", \"200\"]}]', '[{\"token\": \"r.json()[\\\"data\\\"]\"}]', 'Jin', null, '2018-05-09 18:15:55', '2018-05-09 18:15:55');
INSERT INTO `t_testcass` VALUES ('4', '1', '测试流程1', 'testsuite', '2333', '0', '{\"url\": \"http://127.0.0.1:2333/chicktoken\", \"json\": {\"token\": \"$token\"}, \"method\": \"POST\", \"headers\": {\"Content-Type\": \"application/json\"}, \"timeout\": 10}', '[{\"Equal\": [\"r.json()[\\\"code\\\"]\", \"200\"]}, {\"Equal\": [\"r.status_code\", \"200\"]}]', '[]', 'Jin', null, '2018-05-09 18:15:55', '2018-05-09 18:15:55');
