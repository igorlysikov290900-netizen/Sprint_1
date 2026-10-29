types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

tickets_by_type = {}

for key, ticket_list in tickets.items():
    bug_type = types[key]
    unique_tickets = []
    for ticket in ticket_list:
        if ticket not in unique_tickets:
            unique_tickets.append(ticket)

    tickets_by_type[bug_type] = unique_tickets

print(tickets_by_type) 