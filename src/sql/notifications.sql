CREATE TABLE notifications (
    id bigserial NOT NULL,
    description text NULL,
    metadata jsonb NULL,
    title varchar(60) NOT NULL,
    CONSTRAINT notifications_pkey PRIMARY KEY (id)
);
