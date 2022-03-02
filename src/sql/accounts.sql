CREATE TABLE accounts (
    id uuid NOT NULL,
    user_id uuid NOT NULL,
    CONSTRAINT accounts_pkey PRIMARY KEY (id)
);
CREATE INDEX accounts_user_id_7f1e1f1e ON accounts USING btree (user_id);

ALTER TABLE accounts ADD CONSTRAINT accounts_user_id_7f1e1f1e_fk_users_id FOREIGN KEY (user_id) REFERENCES users(id) DEFERRABLE INITIALLY DEFERRED;
