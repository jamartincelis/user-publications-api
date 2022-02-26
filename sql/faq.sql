CREATE TABLE faqs (
    id bigserial NOT NULL,
    question varchar(200) NULL,
    answer text NULL,
    CONSTRAINT faqs_pkey PRIMARY KEY (id)
);
