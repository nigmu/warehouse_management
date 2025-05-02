from tower.models import Tower


def suggest_towers(required_quantity, warehouse=None):
    towers = Tower.objects.all()

    if warehouse:
        # Prioritize towers in same warehouse
        towers = sorted(
            towers,
            key=lambda t: (t.warehouse != warehouse, -t.available_capacity)
        )
    else:
        # Just sort by capacity if no warehouse preference
        towers = sorted(towers, key=lambda t: -t.available_capacity)

    suggestions = []
    remaining = required_quantity

    for tower in towers:
        if tower.available_capacity > 0:
            can_fit = min(tower.available_capacity, remaining)
            suggestions.append((tower, can_fit))
            remaining -= can_fit
        if remaining <= 0:
            break

    return suggestions
