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
