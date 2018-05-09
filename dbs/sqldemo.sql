SELECT
	-- t_product.id as productid,
	-- t_product.product,
	t_project.id as projectid,
	t_project.project,
	t_modules.id as moduleid,
	t_modules.modules,
	t_testcass.id as cassid,
	t_testcass.testname
FROM
	t_project
-- LEFT JOIN t_project ON t_product.id = t_project.productid
LEFT JOIN t_modules ON t_project.id = t_modules.projectid
LEFT JOIN t_testcass ON t_modules.id = t_testcass.moduleid
WHERE t_project.id = 1



SELECT
	t_product.id as productid,
	t_product.product,
	t_product.`explain`,
    (SELECT COUNT(*) FROM t_project WHERE t_project.productid = t_product.id) AS jectnum,
    (SELECT COUNT(*) FROM t_modules WHERE t_modules.projectid = t_project.id) AS modulenum,
	t_product.leader,
	t_product.remark,
    t_product.createtime,
    t_product.updatatime
FROM
	t_product
LEFT JOIN t_project ON t_product.id = t_project.productid
LEFT JOIN t_modules ON t_project.id = t_modules.projectid
-- LEFT JOIN t_testcass ON t_modules.id = t_testcass.moduleid
group by t_product.id



SELECT
	t_project.id as t_projectid,
	t_project.project,
	t_project.`explain`,
    (SELECT COUNT(*) FROM t_modules WHERE t_modules.projectid = t_project.id) AS modulenum,
    (SELECT COUNT(*) FROM t_testcass WHERE t_testcass.moduleid = t_modules.id) AS cassnum,
	t_project.leader,
	t_project.remark,
    t_project.createtime,
    t_project.updatatime
FROM
	t_project
-- LEFT JOIN t_project ON t_product.id = t_project.productid
LEFT JOIN t_modules ON t_project.id = t_modules.projectid
LEFT JOIN t_testcass ON t_modules.id = t_testcass.moduleid
WHERE
    t_project.productid = 2
-- group by t_project.id;





SELECT
    t_modules.id as moduleid,
    t_modules.modules,
    t_modules.`explain`,
    -- (SELECT COUNT(*) FROM t_modules WHERE t_modules.projectid = t_project.id) AS modulenum,
    (SELECT COUNT(*) FROM t_testcass WHERE t_testcass.moduleid = t_modules.id) AS cassnum,
    t_modules.leader,
    t_modules.remark,
    t_modules.createtime,
    t_modules.updatatime
FROM
    t_modules
-- LEFT JOIN t_modules ON t_project.id = t_modules.projectid
LEFT JOIN t_testcass ON t_modules.id = t_testcass.moduleid
-- WHERE t_project.productid = 2\
group by t_modules.id;


SELECT
	t_testcass.id as testid,
	(SELECT modules FROM t_modules WHERE id = t_testcass.moduleid) as modulename,
	t_testcass.testname,
	t_testcass.`explain`,
	t_testcass.status,
	t_testcass.leader,
	t_testcass.remark,
	t_testcass.createtime
FROM
	t_testcass
LEFT JOIN t_modules ON t_testcass.moduleid = t_modules.id


SELECT
	moduleid,
	testname,
	testtype,
	`explain`,
	request,
	validate,
	extract,
	leader,
	remark
FROM t_testcass WHERE id = 1;