/*
Navicat MySQL Data Transfer

Source Server         : MyWeb
Source Server Version : 50719
Source Host           : localhost:3306
Source Database       : nahsor

Target Server Type    : MYSQL
Target Server Version : 50719
File Encoding         : 65001

Date: 2018-05-11 05:49:20
*/

SET FOREIGN_KEY_CHECKS=0;

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of t_modules
-- ----------------------------
INSERT INTO `t_modules` VALUES ('1', '1', '测试模块', 'servers里面写的测试的接口', '浪晋', '没有备注', '2018-05-11 05:43:47', '2018-05-11 05:43:47');

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of t_product
-- ----------------------------
INSERT INTO `t_product` VALUES ('1', 'Nahsor自动化测试平台', '一个接口自动化测试平台，功能强大，很厉害就是了。', '浪晋', '这是例子', '2018-05-11 05:41:08', '2018-05-11 05:41:08');

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of t_project
-- ----------------------------
INSERT INTO `t_project` VALUES ('1', '1', 'Nahsor自动化测试平台WEB端', '功能强大，厉害的不行', '浪晋', '没有备注', '2018-05-11 05:42:30', '2018-05-11 05:42:30');

-- ----------------------------
-- Table structure for t_reports
-- ----------------------------
DROP TABLE IF EXISTS `t_reports`;
CREATE TABLE `t_reports` (
  `id` int(16) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `cassid` int(16) NOT NULL COMMENT '用例id',
  `status` int(8) DEFAULT NULL COMMENT '状态，0：成功 1：失败 2：报错',
  `result` varchar(255) DEFAULT NULL COMMENT '执行结果',
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '运行时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_reports
-- ----------------------------

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
  `request` json NOT NULL COMMENT '请求参数',
  `validate` json DEFAULT NULL COMMENT '校验参数',
  `extract` json DEFAULT NULL COMMENT '提取参数',
  `leader` varchar(255) DEFAULT NULL COMMENT '负责人',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatatime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_testcass
-- ----------------------------
