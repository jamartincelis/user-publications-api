CREATE TABLE codes (
    id uuid NOT NULL,
    "name" varchar(60) NOT NULL,
    description varchar(100) NULL,
    metadata jsonb NULL,
    created_at timestamptz NOT NULL,
    updated_at timestamptz NOT NULL,
    code_type_id uuid NOT NULL,
    CONSTRAINT codes_pkey PRIMARY KEY (id)
);
CREATE INDEX codes_code_type_id_b15df7c7 ON codes USING btree (code_type_id);

ALTER TABLE codes ADD CONSTRAINT codes_code_type_id_b15df7c7_fk_codetypes_id FOREIGN KEY (code_type_id) REFERENCES codetypes(id) DEFERRABLE INITIALLY DEFERRED;
