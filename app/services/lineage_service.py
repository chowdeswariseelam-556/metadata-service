
from sqlalchemy.orm import Session
from app.models.lineage import Lineage

def has_cycle(db: Session, source: str, target: str):

    visited = set()

    def dfs(node):
        if node == source:
            return True

        visited.add(node)

        children = db.query(Lineage).filter(
            Lineage.upstream_fqn == node
        ).all()

        for child in children:
            if child.downstream_fqn not in visited:
                if dfs(child.downstream_fqn):
                    return True

        return False

    return dfs(target)
