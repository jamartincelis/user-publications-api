CREATE TABLE codetypes (
    id uuid NOT NULL,
    "name" varchar(60) NOT NULL,
    description varchar(100) NULL,
    created_at timestamptz NOT NULL,
    updated_at timestamptz NOT NULL,
    CONSTRAINT codetypes_pkey PRIMARY KEY (id)
);
