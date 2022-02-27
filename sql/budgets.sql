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
