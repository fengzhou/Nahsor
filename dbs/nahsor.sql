/*
 Navicat Premium Data Transfer

 Source Server         : 本机
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : nahsor

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 09/05/2018 18:27:07
*/

DROP DATABASE IF EXISTS nahsor;
CREATE DATABASE nahsor DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_general_ci;
USE nahsor;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_config
-- ----------------------------
DROP TABLE IF EXISTS `t_config`;
CREATE TABLE `t_config`  (
  `id` int(11) NOT NULL,
  `url` json NULL,
  `headers` json NULL,
  `method` json NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_config
-- ----------------------------
INSERT INTO `t_config` VALUES (1, '[\"www.baidu.com\"]', '{\"content-type\": \"application/json\"}', '[\"POST\", \"GET\"]');

-- ----------------------------
-- Table structure for t_modules
-- ----------------------------
DROP TABLE IF EXISTS `t_modules`;
CREATE TABLE `t_modules`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `productid` int(16) NOT NULL COMMENT '所属产品ID',
  `projectid` int(16) NOT NULL COMMENT '所属项目id',
  `modules` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '模块名称',
  `explain` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '描述',
  `leader` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '负责人',
  `remark` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '备注',
  `createtime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `updatatime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `modules`(`modules`) USING BTREE,
  INDEX `project`(`projectid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_modules
-- ----------------------------
INSERT INTO `t_modules` VALUES (1, 1, 1, '测试模块', '描述', '责任人', '备注', '2018-05-03 14:55:01', '2018-05-03 14:55:01');
INSERT INTO `t_modules` VALUES (2, 1, 1, '测试模块', '描述', '责任人', '备注', '2018-05-03 14:55:08', '2018-05-03 14:55:08');
INSERT INTO `t_modules` VALUES (3, 2, 1, '测试模块', '描述', '责任人', '备注', '2018-05-03 14:55:09', '2018-05-03 14:55:09');
INSERT INTO `t_modules` VALUES (4, 2, 1, '测试模块', '描述', '责任人', '备注', '2018-05-03 14:55:16', '2018-05-03 14:55:16');

-- ----------------------------
-- Table structure for t_product
-- ----------------------------
DROP TABLE IF EXISTS `t_product`;
CREATE TABLE `t_product`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `product` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '产品名称',
  `explain` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '负责人',
  `leader` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '状态，0可用，1不可用',
  `remark` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '说明，描述',
  `createtime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `updatatime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `product`(`product`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_product
-- ----------------------------
INSERT INTO `t_product` VALUES (1, '测试产品1', '描述', '责任人', '备注', '2018-05-03 13:11:04', '2018-05-03 13:11:04');
INSERT INTO `t_product` VALUES (2, '产品名称22', '描述1112', '责任人2', '备注1', '2018-05-06 04:26:20', '2018-05-06 04:26:20');

-- ----------------------------
-- Table structure for t_project
-- ----------------------------
DROP TABLE IF EXISTS `t_project`;
CREATE TABLE `t_project`  (
  `id` int(16) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `productid` int(16) NOT NULL COMMENT '关联的产品id',
  `project` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '项目名称',
  `explain` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '描述',
  `leader` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '负责人',
  `remark` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '备注',
  `createtime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `updatatime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `project`(`project`) USING BTREE,
  INDEX `product`(`productid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_project
-- ----------------------------
INSERT INTO `t_project` VALUES (1, 2, '项目名称1', '描述', '负责人', '备注', '2018-05-03 13:59:35', '2018-05-03 13:59:35');
INSERT INTO `t_project` VALUES (2, 2, '项目名称2', '描述', '负责人', '备注', '2018-05-03 13:59:36', '2018-05-03 13:59:36');
INSERT INTO `t_project` VALUES (3, 1, '项目名称3', '描述', '负责人', '备注', '2018-05-03 13:59:42', '2018-05-03 13:59:42');

-- ----------------------------
-- Table structure for t_testcass
-- ----------------------------
DROP TABLE IF EXISTS `t_testcass`;
CREATE TABLE `t_testcass`  (
  `id` int(16) NOT NULL AUTO_INCREMENT,
  `productid` int(16) NOT NULL COMMENT '所属产品id',
  `projectid` int(16) NOT NULL COMMENT '所属项目id',
  `moduleid` int(16) NOT NULL COMMENT '所属模块id',
  `testname` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用例名称',
  `modules` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '所属功能模块',
  `testtype` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用例类型',
  `request` json NOT NULL COMMENT '请求参数',
  `validate` json NULL COMMENT '校验参数',
  `extract` json NULL COMMENT '提取参数',
  `leader` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '负责人',
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注',
  `createtime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `updatatime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '修改时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `modules`(`modules`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_testcass
-- ----------------------------
INSERT INTO `t_testcass` VALUES (1, 0, 0, 0, 'tastcass110', '1', 'testcass', '{\"url\": \"http://127.0.0.1:2333/tes1t\", \"json\": {\"aaa\": \"bbb\"}, \"method\": \"POST\", \"headers\": {\"Content-Type\": \"application/json\"}, \"timeout\": 10}', '[{\"Equal\": [\"r.json()\", \"request[\\\"json\\\"]\"]}, {\"Equal\": [\"r.status_code\", \"200\"]}]', '{}', 'Jin', '2333', '2018-05-09 18:26:49', '2018-05-09 18:26:49');
INSERT INTO `t_testcass` VALUES (2, 0, 0, 0, 'tastcass210', '1', 'testcass', '{\"url\": \"http://127.0.0.1:2333/test\", \"json\": {\"aaa\": \"bbb\"}, \"method\": \"POST\", \"headers\": {\"Content-Type\": \"application/json\"}, \"timeout\": 10}', '[{\"Equal\": [\"r.json()\", \"request[\\\"json\\\"]\"]}, {\"Equal\": [\"r.status_code\", \"201\"]}]', '{}', 'Jin', '2333', '2018-05-09 18:26:52', '2018-05-09 18:26:52');
INSERT INTO `t_testcass` VALUES (3, 0, 0, 0, '测试流程', '1', 'testsuite', '{\"url\": \"http://127.0.0.1:2333/login\", \"json\": {\"password\": \"123456\", \"username\": \"admin\"}, \"method\": \"POST\", \"headers\": {\"Content-Type\": \"application/json\"}, \"timeout\": 10}', '[{\"Equal\": [\"r.status_code\", \"200\"]}]', '[{\"token\": \"r.json()[\\\"data\\\"]\"}]', 'Jin', NULL, '2018-05-03 16:20:35', '2018-05-03 16:20:35');
INSERT INTO `t_testcass` VALUES (4, 0, 0, 0, '测试流程1', '1', 'testsuite', '{\"url\": \"http://127.0.0.1:2333/chicktoken\", \"json\": {\"token\": \"$token\"}, \"method\": \"POST\", \"headers\": {\"Content-Type\": \"application/json\"}, \"timeout\": 10}', '[{\"Equal\": [\"r.json()[\\\"code\\\"]\", \"200\"]}, {\"Equal\": [\"r.status_code\", \"200\"]}]', '[]', 'Jin', NULL, '2018-05-03 16:20:35', '2018-05-03 16:20:35');

SET FOREIGN_KEY_CHECKS = 1;
