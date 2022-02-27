CREATE TABLE transactions (
    id uuid NOT NULL,
    amount numeric(12, 2) NOT NULL,
    description varchar(100) NOT NULL,
    transaction_date timestamptz NOT NULL,
    category_id uuid NULL,
    user_note varchar(100) NULL,
    account_id uuid NOT NULL,
    PRIMARY KEY (id, transaction_date)
) PARTITION BY RANGE (transaction_date);

CREATE TABLE transactions_202201 PARTITION OF transactions FOR VALUES FROM ('2022-01-01') TO ('2022-02-01');
CREATE TABLE transactions_202202 PARTITION OF transactions FOR VALUES FROM ('2022-02-01') TO ('2022-03-01');
CREATE TABLE transactions_202203 PARTITION OF transactions FOR VALUES FROM ('2022-03-01') TO ('2022-04-01');
CREATE TABLE transactions_202204 PARTITION OF transactions FOR VALUES FROM ('2022-04-01') TO ('2022-05-01');
CREATE TABLE transactions_202205 PARTITION OF transactions FOR VALUES FROM ('2022-05-01') TO ('2022-06-01');
CREATE TABLE transactions_202206 PARTITION OF transactions FOR VALUES FROM ('2022-06-01') TO ('2022-07-01');
CREATE TABLE transactions_202207 PARTITION OF transactions FOR VALUES FROM ('2022-07-01') TO ('2022-08-01');
CREATE TABLE transactions_202208 PARTITION OF transactions FOR VALUES FROM ('2022-08-01') TO ('2022-09-01');
CREATE TABLE transactions_202209 PARTITION OF transactions FOR VALUES FROM ('2022-09-01') TO ('2022-10-01');
CREATE TABLE transactions_202210 PARTITION OF transactions FOR VALUES FROM ('2022-10-01') TO ('2022-11-01');
CREATE TABLE transactions_202211 PARTITION OF transactions FOR VALUES FROM ('2022-11-01') TO ('2022-12-01');
CREATE TABLE transactions_202212 PARTITION OF transactions FOR VALUES FROM ('2022-12-01') TO ('2023-01-01');
CREATE TABLE transactions_202301 PARTITION OF transactions FOR VALUES FROM ('2023-01-01') TO ('2023-02-01');
CREATE TABLE transactions_202302 PARTITION OF transactions FOR VALUES FROM ('2023-02-01') TO ('2023-03-01');
CREATE TABLE transactions_202303 PARTITION OF transactions FOR VALUES FROM ('2023-03-01') TO ('2023-04-01');
CREATE TABLE transactions_202304 PARTITION OF transactions FOR VALUES FROM ('2023-04-01') TO ('2023-05-01');


CREATE INDEX transactions_account_id_d92b47af ON transactions USING btree (account_id);
CREATE INDEX transactions_category_id_65740af9 ON transactions USING btree (category_id);

ALTER TABLE transactions ADD CONSTRAINT transactions_account_id_d92b47af_fk_accounts_id FOREIGN KEY (account_id) REFERENCES accounts(id) DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE transactions ADD CONSTRAINT transactions_category_id_65740af9_fk_codes_id FOREIGN KEY (category_id) REFERENCES codes(id) DEFERRABLE INITIALLY DEFERRED;

CREATE TABLE budgets (
    id uuid NOT NULL,
    budget_date date NOT NULL,
    category_id uuid NOT NULL,
    user_id uuid NOT NULL,
    amount numeric(12, 2) NOT NULL,
    CONSTRAINT budgets_pkey PRIMARY KEY (id)
);
CREATE INDEX budgets_category_id_328a159f ON budgets USING btree (category_id);
CREATE INDEX budgets_user_id_d4bb9f71 ON budgets USING btree (user_id);

CREATE TABLE faqs (
    id bigserial NOT NULL,
    question varchar(200) NULL,
    answer text NULL,
    CONSTRAINT faqs_pkey PRIMARY KEY (id)
);

CREATE TABLE monthly_summaries (
    id uuid NOT NULL,
    incomes_sum numeric(12, 2) NOT NULL,
    incomes_count int2 NOT NULL,
    expenses_sum numeric(12, 2) NOT NULL,
    expenses_count int2 NOT NULL,
    balance numeric(12, 2) NOT NULL,
    summary_date timestamptz NOT NULL,
    user_id uuid NOT NULL,
    CONSTRAINT monthly_summaries_pkey PRIMARY KEY (id)
);
CREATE INDEX monthly_summaries_user_id_9a827774 ON monthly_summaries USING btree (user_id);

CREATE TABLE notifications (
    id bigserial NOT NULL,
    description text NULL,
    metadata jsonb NULL,
    title varchar(60) NOT NULL,
    CONSTRAINT notifications_pkey PRIMARY KEY (id)
);

CREATE TABLE tips (
    id bigserial NOT NULL,
    title varchar(60) NOT NULL,
    description text NULL,
    metadata jsonb NULL,
    CONSTRAINT tips_pkey PRIMARY KEY (id)
);
