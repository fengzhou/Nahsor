/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : nahsor

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 26/04/2018 22:53:13
*/


DROP DATABASE IF EXISTS nahsor;
CREATE DATABASE nahsor DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_general_ci;


USE nahsor;



SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_testcass
-- ----------------------------
DROP TABLE IF EXISTS `t_testcass`;
CREATE TABLE `t_testcass`  (
  `id` int(16) NOT NULL AUTO_INCREMENT,
  `cassname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用例名称',
  `testcass` json NOT NULL COMMENT '用例内容，以json格式储存',
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '备注',
  `createtime` datetime(0) DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `updatatime` datetime(0) DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '修改时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_testcass
-- ----------------------------
INSERT INTO `t_testcass` VALUES (1, 'tastcass', '{\"req\": {\"url\": \"http://127.0.0.1:2333/test\", \"json\": {\"aaa\": \"bbb\"}, \"method\": \"GET\", \"headers\": {\"Content-Type\": \"application/json\"}, \"timeout\": 10}, \"cass_name\": \"test_name\", \"validates\": [{\"Equal\": [\"r.json()\", \"req[\\\"json\\\"]\"]}, {\"Equal\": [\"r.status_code\", \"200\"]}]}', '2333', '2018-04-26 22:50:25', '2018-04-26 22:50:25');
INSERT INTO `t_testcass` VALUES (2, 'tastcass', '{\"req\": {\"url\": \"http://127.0.0.1:2333/test\", \"json\": {\"aaa\": \"bbb\"}, \"method\": \"GET\", \"headers\": {\"Content-Type\": \"application/json\"}, \"timeout\": 10}, \"cass_name\": \"test_name111\", \"validates\": [{\"Equal\": [\"r.json()\", \"req[\\\"json\\\"]\"]}, {\"Equal\": [\"r.status_code\", \"201\"]}]}', '2333', '2018-04-26 22:50:29', '2018-04-26 22:50:29');

SET FOREIGN_KEY_CHECKS = 1;
