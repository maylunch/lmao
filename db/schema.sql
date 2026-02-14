CREATE TABLE users (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) UNIQUE,
  phone VARCHAR(50) UNIQUE,
  password_hash VARCHAR(255),
  vip_level INT DEFAULT 0,
  vip_expire_at DATETIME,
  trial_used BOOLEAN DEFAULT FALSE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE accounts (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT,
  name VARCHAR(100),
  base_currency VARCHAR(10),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE positions (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  account_id BIGINT,
  stock_code VARCHAR(20),
  market VARCHAR(20),
  quantity DECIMAL(20,4),
  avg_cost DECIMAL(20,4),
  leverage_ratio DECIMAL(10,4),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE daily_snapshots (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  position_id BIGINT,
  date DATE,
  close_price DECIMAL(20,4),
  market_value DECIMAL(20,4),
  unrealized_pnl DECIMAL(20,4)
);

CREATE TABLE stock_master (
  stock_code VARCHAR(20) PRIMARY KEY,
  stock_name VARCHAR(100),
  market VARCHAR(20),
  industry VARCHAR(50),
  currency VARCHAR(10)
);

CREATE TABLE index_data (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  index_code VARCHAR(20),
  index_name VARCHAR(50),
  date DATE,
  close_price DECIMAL(20,4)
);

CREATE TABLE ai_reports (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT,
  report_type VARCHAR(50),
  risk_score INT,
  suggestion_summary VARCHAR(1000),
  full_report_json JSON,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE payment_orders (
  order_no VARCHAR(64) PRIMARY KEY,
  user_id BIGINT,
  amount DECIMAL(10,2),
  pay_channel VARCHAR(20),
  status VARCHAR(20),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);