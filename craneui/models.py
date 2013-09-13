from docker import client

def create_container(host
                    ,image
                    ,environment
                    ,memory
                    ,description
                    ,volumes
                    ,volumes_from
                    ,privileged
                    ,owner
                    ,binds):
    c = host._get_client()
    cnt = c.create_container(image
                            ,None
                            ,detach=True
                            ,ports=ports
                            ,mem_limit=memory
                            ,tty=True
                            ,stdin_open=True
                            ,environment=environment
                            ,volumes=volumes
                            ,volumes_from=volumes_from
                            ,privileged=privileged)
    c_id = cnt.get('Id')
    c.start(c_id, binds)
    status = False
    # create metadata only if container starts successfully
    if c.inspect_container(c_id).get('State', {}).get('Running'):
       c, created = Container.objects.get_or_create(container_id=c_id,
                                                    host=host)
       c.description = description
       c.owner = owner
       c.save()
       status = True
       # clear host cache
       host._invalidate_container_cache()
