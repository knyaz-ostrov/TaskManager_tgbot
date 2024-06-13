CREATE TABLE IF NOT EXISTS public.tasks
(
    id SERIAL PRIMARY KEY,
    username text COLLATE pg_catalog."default",
    user_id bigint,
    task text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tasks
    OWNER to %(user)s;
