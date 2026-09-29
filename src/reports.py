def search_complaints(complaints, keyword):
    keyword = keyword.strip().lower()

    if not keyword:
        return []

    results = []

    for complaint in complaints:
        if (
            keyword in complaint.title.lower()
            or keyword in complaint.description.lower()
            or keyword in complaint.category.lower()
            or keyword in complaint.status.lower()
        ):
            results.append(complaint)

    return results


def filter_by_category(complaints, category):
    return [
        complaint
        for complaint in complaints
        if complaint.category == category
    ]


def get_statistics(complaints):
    statistics = {
        "total": len(complaints),
        "pending": 0,
        "in_progress": 0,
        "resolved": 0,
        "high_priority": 0
    }

    for complaint in complaints:
        if complaint.status == "Pending":
            statistics["pending"] += 1
        elif complaint.status == "In Progress":
            statistics["in_progress"] += 1
        elif complaint.status == "Resolved":
            statistics["resolved"] += 1

        if complaint.priority == "High":
            statistics["high_priority"] += 1

    return statistics
