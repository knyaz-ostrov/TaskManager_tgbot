CREATE TABLE IF NOT EXISTS public.tasks
(
    username text COLLATE pg_catalog."default",
    user_id bigint,
    task text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tasks
    OWNER to %(user)s;