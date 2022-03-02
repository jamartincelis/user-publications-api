CREATE TABLE users (
    id uuid NOT NULL,
    optional_id varchar(60) NOT NULL,
    email varchar(254) NULL,
    CONSTRAINT users_pkey PRIMARY KEY (id)
);
