-- 创建fake_token表
DROP TABLE IF EXISTS fake_token ;
DROP TABLE IF EXISTS real_token;
CREATE TABLE fake_token (
  id INT,
  name STRING,
  token STRING
);

-- 创建real_token表
CREATE TABLE real_token (
  id INT,
  name STRING,
  token STRING
);

-- 插入数据到fake_token表
INSERT INTO fake_token (id, name, token) VALUES (1, 'ctfer', 'nonono_fake_token');

-- 插入数据到real_token表
INSERT INTO real_token (id, name, token) VALUES (1, 'Em4non', 'hit_si11y_Drunkbaby');