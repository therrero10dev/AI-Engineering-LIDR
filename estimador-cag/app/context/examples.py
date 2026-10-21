# Ejemplos precargados que se inyectan en el contexto (CAG).
EXAMPLES: list[dict[str, str]] = [
    {
        "meeting_summary": (
            "El cliente necesita una app móvil para reservar citas en su cadena "
            "de clínicas dentales. Los pacientes deben poder ver disponibilidad "
            "por sucursal, reservar, cancelar y recibir recordatorios por push y "
            "email. El personal administrativo necesita un panel web para "
            "gestionar agendas y doctores."
        ),
        "estimation": """
        ## Estimación: App de Reservas para Clínicas Dentales

        ### Desglose de tareas:
        1. Diseño UI/UX (app y panel web): 50 horas
        2. Backend API (citas, sucursales, doctores): 70 horas
        3. App móvil (iOS y Android, cross-platform): 90 horas
        4. Panel web de administración: 45 horas
        5. Notificaciones push y email: 20 horas
        6. Autenticación y roles: 20 horas
        7. Testing y QA: 35 horas

        **Total estimado: 330 horas**
        **Equipo recomendado: 2 desarrolladores móviles/full-stack + 1 backend + 1 diseñador UX (part-time)**
        **Duración estimada: 10-12 semanas**
        """,
    },
    {
        "meeting_summary": (
            "Una cadena de peluquerías y centros de estética quiere una "
            "aplicación web para que los clientes reserven citas con un "
            "profesional concreto, elijan servicios con duración variable y "
            "paguen un anticipo online. Los profesionales deben poder gestionar "
            "su calendario y bloquear horarios. Se requiere sincronización con "
            "Google Calendar y recordatorios por SMS."
        ),
        "estimation": """
        ## Estimación: Plataforma Web de Reservas para Peluquerías y Centros de Estética

        ### Desglose de tareas:
        1. Diseño UI/UX (flujo de reserva y panel de profesionales): 40 horas
        2. Backend API (servicios, profesionales, disponibilidad, citas): 65 horas
        3. Motor de disponibilidad con servicios de duración variable: 25 horas
        4. Frontend web de reserva (responsive): 55 horas
        5. Panel de profesionales (calendario y bloqueos): 40 horas
        6. Pagos online de anticipo (Stripe): 25 horas
        7. Sincronización con Google Calendar: 20 horas
        8. Recordatorios por SMS: 15 horas
        9. Testing y QA: 30 horas

        **Total estimado: 315 horas**
        **Equipo recomendado: 2 desarrolladores full-stack + 1 diseñador UX (part-time)**
        **Duración estimada: 9-11 semanas**
        """,
    },
]
