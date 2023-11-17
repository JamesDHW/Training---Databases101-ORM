class ShardingRouter:
    def db_for_read(self, model, **hints):
        instance = hints.get('instance')
        if instance and hasattr(instance, 'shard_id'):
            return instance.shard_id
        return None

    def db_for_write(self, model, **hints):
        instance = hints.get('instance')
        if instance and hasattr(instance, 'shard_id'):
            return instance.shard_id
        return None
