CREATE TABLE tips (
    id bigserial NOT NULL,
    title varchar(60) NOT NULL,
    description text NULL,
    metadata jsonb NULL,
    CONSTRAINT tips_pkey PRIMARY KEY (id)
);
