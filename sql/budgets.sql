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

ALTER TABLE budgets ADD CONSTRAINT budgets_category_id_328a159f_fk_codes_id FOREIGN KEY (category_id) REFERENCES codes(id) DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE budgets ADD CONSTRAINT budgets_user_id_d4bb9f71_fk_users_id FOREIGN KEY (user_id) REFERENCES users(id) DEFERRABLE INITIALLY DEFERRED;
