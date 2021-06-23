# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
METRIC_MAP = {
    'haproxy_backend_active_servers': 'backend.active.servers',
    'haproxy_backend_backup_servers': 'backend.backup.servers',
    'haproxy_backend_bytes_in_total': 'backend.bytes.in.total',
    'haproxy_backend_bytes_out_total': 'backend.bytes.out.total',
    'haproxy_backend_check_last_change_seconds': 'backend.check.last.change.seconds',
    'haproxy_backend_check_up_down_total': 'backend.check.up.down.total',
    'haproxy_backend_client_aborts_total': 'backend.client.aborts.total',
    'haproxy_backend_connection_attempts_total': 'backend.connection.attempts.total',
    'haproxy_backend_connection_errors_total': 'backend.connection.errors.total',
    'haproxy_backend_connection_reuses_total': 'backend.connection.reuses.total',
    'haproxy_backend_connect_time_average_seconds': 'backend.connect.time.average.seconds',
    'haproxy_backend_current_queue': 'backend.current.queue',
    'haproxy_backend_current_sessions': 'backend.current.sessions',
    'haproxy_backend_downtime_seconds_total': 'backend.downtime.seconds.total',
    'haproxy_backend_failed_header_rewriting_total': 'backend.failed.header.rewriting.total',
    'haproxy_backend_http_cache_hits_total': 'backend.http.cache.hits.total',
    'haproxy_backend_http_cache_lookups_total': 'backend.http.cache.lookups.total',
    'haproxy_backend_http_comp_bytes_bypassed_total': 'backend.http.comp.bytes.bypassed.total',
    'haproxy_backend_http_comp_bytes_in_total': 'backend.http.comp.bytes.in.total',
    'haproxy_backend_http_comp_bytes_out_total': 'backend.http.comp.bytes.out.total',
    'haproxy_backend_http_comp_responses_total': 'backend.http.comp.responses.total',
    'haproxy_backend_http_requests_total': 'backend.http.requests.total',
    'haproxy_backend_http_responses_total': 'backend.http.responses.total',
    'haproxy_backend_internal_errors_total': 'backend.internal.errors.total',
    'haproxy_backend_last_session_seconds': 'backend.last.session.seconds',
    'haproxy_backend_limit_sessions': 'backend.limit.sessions',
    'haproxy_backend_loadbalanced_total': 'backend.loadbalanced.total',
    'haproxy_backend_max_connect_time_seconds': 'backend.max.connect.time.seconds',
    'haproxy_backend_max_queue': 'backend.max.queue',
    'haproxy_backend_max_queue_time_seconds': 'backend.max.queue.time.seconds',
    'haproxy_backend_max_response_time_seconds': 'backend.max.response.time.seconds',
    'haproxy_backend_max_session_rate': 'backend.max.session.rate',
    'haproxy_backend_max_sessions': 'backend.max.sessions',
    'haproxy_backend_max_total_time_seconds': 'backend.max.total.time.seconds',
    'haproxy_backend_queue_time_average_seconds': 'backend.queue.time.average.seconds',
    'haproxy_backend_redispatch_warnings_total': 'backend.redispatch.warnings.total',
    'haproxy_backend_requests_denied_total': 'backend.requests.denied.total',
    'haproxy_backend_response_errors_total': 'backend.response.errors.total',
    'haproxy_backend_responses_denied_total': 'backend.responses.denied.total',
    'haproxy_backend_response_time_average_seconds': 'backend.response.time.average.seconds',
    'haproxy_backend_retry_warnings_total': 'backend.retry.warnings.total',
    'haproxy_backend_server_aborts_total': 'backend.server.aborts.total',
    'haproxy_backend_sessions_total': 'backend.sessions.total',
    'haproxy_backend_status': 'backend.status',
    'haproxy_backend_total_time_average_seconds': 'backend.total.time.average.seconds',
    'haproxy_backend_uweight': 'backend.uweight',
    'haproxy_backend_weight': 'backend.weight',
    'haproxy_frontend_bytes_in_total': 'frontend.bytes.in.total',
    'haproxy_frontend_bytes_out_total': 'frontend.bytes.out.total',
    'haproxy_frontend_connections_rate_max': 'frontend.connections.rate.max',
    'haproxy_frontend_connections_total': 'frontend.connections.total',
    'haproxy_frontend_current_sessions': 'frontend.current.sessions',
    'haproxy_frontend_denied_connections_total': 'frontend.denied.connections.total',
    'haproxy_frontend_denied_sessions_total': 'frontend.denied.sessions.total',
    'haproxy_frontend_failed_header_rewriting_total': 'frontend.failed.header.rewriting.total',
    'haproxy_frontend_http_cache_hits_total': 'frontend.http.cache.hits.total',
    'haproxy_frontend_http_cache_lookups_total': 'frontend.http.cache.lookups.total',
    'haproxy_frontend_http_comp_bytes_bypassed_total': 'frontend.http.comp.bytes.bypassed.total',
    'haproxy_frontend_http_comp_bytes_in_total': 'frontend.http.comp.bytes.in.total',
    'haproxy_frontend_http_comp_bytes_out_total': 'frontend.http.comp.bytes.out.total',
    'haproxy_frontend_http_comp_responses_total': 'frontend.http.comp.responses.total',
    'haproxy_frontend_http_requests_rate_max': 'frontend.http.requests.rate.max',
    'haproxy_frontend_http_requests_total': 'frontend.http.requests.total',
    'haproxy_frontend_http_responses_total': 'frontend.http.responses.total',
    'haproxy_frontend_intercepted_requests_total': 'frontend.intercepted.requests.total',
    'haproxy_frontend_internal_errors_total': 'frontend.internal.errors.total',
    'haproxy_frontend_limit_session_rate': 'frontend.limit.session.rate',
    'haproxy_frontend_limit_sessions': 'frontend.limit.sessions',
    'haproxy_frontend_max_session_rate': 'frontend.max.session.rate',
    'haproxy_frontend_max_sessions': 'frontend.max.sessions',
    'haproxy_frontend_request_errors_total': 'frontend.request.errors.total',
    'haproxy_frontend_requests_denied_total': 'frontend.requests.denied.total',
    'haproxy_frontend_responses_denied_total': 'frontend.responses.denied.total',
    'haproxy_frontend_sessions_total': 'frontend.sessions.total',
    'haproxy_frontend_status': 'frontend.status',
    'haproxy_process_active_peers': 'process.active.peers',
    'haproxy_process_build_info': 'process.build_info',
    'haproxy_process_busy_polling_enabled': 'process.busy.polling.enabled',
    'haproxy_process_bytes_out_rate': 'process.bytes.out.rate',
    'haproxy_process_bytes_out_total': 'process.bytes.out.total',
    'haproxy_process_connected_peers': 'process.connected.peers',
    'haproxy_process_connections_total': 'process.connections.total',
    'haproxy_process_current_backend_ssl_key_rate': 'process.current.backend.ssl.key.rate',
    'haproxy_process_current_connection_rate': 'process.current.connection.rate',
    'haproxy_process_current_connections': 'process.current.connections',
    'haproxy_process_current_frontend_ssl_key_rate': 'process.current.frontend.ssl.key.rate',
    'haproxy_process_current_run_queue': 'process.current.run.queue',
    'haproxy_process_current_session_rate': 'process.current.session.rate',
    'haproxy_process_current_ssl_connections': 'process.current.ssl.connections',
    'haproxy_process_current_ssl_rate': 'process.current.ssl.rate',
    'haproxy_process_current_tasks': 'process.current.tasks',
    'haproxy_process_current_zlib_memory': 'process.current.zlib.memory',
    'haproxy_process_dropped_logs_total': 'process.dropped.logs.total',
    'haproxy_process_failed_resolutions': 'process.failed.resolutions',
    'haproxy_process_frontend_ssl_reuse': 'process.frontend.ssl.reuse',
    'haproxy_process_hard_max_connections': 'process.hard.max.connections',
    'haproxy_process_http_comp_bytes_in_total': 'process.http.comp.bytes.in.total',
    'haproxy_process_http_comp_bytes_out_total': 'process.http.comp.bytes.out.total',
    'haproxy_process_idle_time_percent': 'process.idle.time.percent',
    'haproxy_process_jobs': 'process.jobs',
    'haproxy_process_limit_connection_rate': 'process.limit.connection.rate',
    'haproxy_process_limit_http_comp': 'process.limit.http.comp',
    'haproxy_process_limit_session_rate': 'process.limit.session.rate',
    'haproxy_process_limit_ssl_rate': 'process.limit.ssl.rate',
    'haproxy_process_listeners': 'process.listeners',
    'haproxy_process_max_backend_ssl_key_rate': 'process.max.backend.ssl.key.rate',
    'haproxy_process_max_connection_rate': 'process.max.connection.rate',
    'haproxy_process_max_connections': 'process.max.connections',
    'haproxy_process_max_fds': 'process.max.fds',
    'haproxy_process_max_frontend_ssl_key_rate': 'process.max.frontend.ssl.key.rate',
    'haproxy_process_max_memory_bytes': 'process.max.memory.bytes',
    'haproxy_process_max_pipes': 'process.max.pipes',
    'haproxy_process_max_session_rate': 'process.max.session.rate',
    'haproxy_process_max_sockets': 'process.max.sockets',
    'haproxy_process_max_ssl_connections': 'process.max.ssl.connections',
    'haproxy_process_max_ssl_rate': 'process.max.ssl.rate',
    'haproxy_process_max_zlib_memory': 'process.max.zlib.memory',
    'haproxy_process_nbproc': 'process.nbproc',
    'haproxy_process_nbthread': 'process.nbthread',
    'haproxy_process_pipes_free_total': 'process.pipes.free.total',
    'haproxy_process_pipes_used_total': 'process.pipes.used.total',
    'haproxy_process_pool_allocated_bytes': 'process.pool.allocated.bytes',
    'haproxy_process_pool_failures_total': 'process.pool.failures.total',
    'haproxy_process_pool_used_bytes': 'process.pool.used.bytes',
    'haproxy_process_recv_logs_total': 'process.recv.logs.total',
    'haproxy_process_relative_process_id': 'process.relative.process.id',
    'haproxy_process_requests_total': 'process.requests.total',
    'haproxy_process_spliced_bytes_out_total': 'process.spliced.bytes.out.total',
    'haproxy_process_ssl_cache_lookups_total': 'process.ssl.cache.lookups.total',
    'haproxy_process_ssl_cache_misses_total': 'process.ssl.cache.misses.total',
    'haproxy_process_ssl_connections_total': 'process.ssl.connections.total',
    'haproxy_process_start_time_seconds': 'process.start.time.seconds',
    'haproxy_process_stopping': 'process.stopping',
    'haproxy_process_unstoppable_jobs': 'process.unstoppable.jobs',
    'haproxy_process_uptime_seconds': 'process.uptime.seconds',
    'haproxy_listener_bytes_in_total': 'listener.bytes.in.total',
    'haproxy_listener_bytes_out_total': 'listener.bytes.out.total',
    'haproxy_listener_current_sessions': 'listener.current.sessions',
    'haproxy_listener_denied_connections_total': 'listener.denied.connections.total',
    'haproxy_listener_denied_sessions_total': 'listener.denied.sessions.total',
    'haproxy_listener_failed_header_rewriting_total': 'listener.failed.header.rewriting.total',
    'haproxy_listener_internal_errors_total': 'listener.internal.errors.total',
    'haproxy_listener_limit_sessions': 'listener.limit.sessions',
    'haproxy_listener_max_sessions': 'listener.max.sessions',
    'haproxy_listener_request_errors_total': 'listener.request.errors.total',
    'haproxy_listener_requests_denied_total': 'listener.requests.denied.total',
    'haproxy_listener_responses_denied_total': 'listener.responses.denied.total',
    'haproxy_listener_sessions_total': 'listener.sessions.total',
    'haproxy_listener_status': 'listener.status',
    'haproxy_server_bytes_in_total': 'server.bytes.in.total',
    'haproxy_server_bytes_out_total': 'server.bytes.out.total',
    'haproxy_server_check_code': 'server.check.code',
    'haproxy_server_check_duration_seconds': 'server.check.duration.seconds',
    'haproxy_server_check_failures_total': 'server.check.failures.total',
    'haproxy_server_check_last_change_seconds': 'server.check.last.change.seconds',
    'haproxy_server_check_status': 'server.check.status',
    'haproxy_server_check_up_down_total': 'server.check.up.down.total',
    'haproxy_server_client_aborts_total': 'server.client.aborts.total',
    'haproxy_server_connection_attempts_total': 'server.connection.attempts.total',
    'haproxy_server_connection_errors_total': 'server.connection.errors.total',
    'haproxy_server_connection_reuses_total': 'server.connection.reuses.total',
    'haproxy_server_connect_time_average_seconds': 'server.connect.time.average.seconds',
    'haproxy_server_current_queue': 'server.current.queue',
    'haproxy_server_current_sessions': 'server.current.sessions',
    'haproxy_server_current_throttle': 'server.current.throttle',
    'haproxy_server_downtime_seconds_total': 'server.downtime.seconds.total',
    'haproxy_server_failed_header_rewriting_total': 'server.failed.header.rewriting.total',
    'haproxy_server_http_responses_total': 'server.http.responses.total',
    'haproxy_server_server_idle_connections_current': 'server.server.idle.connections.current',
    'haproxy_server_idle_connections_current': 'server.idle.connections.current',  # rename since >= v2.3
    'haproxy_server_server_idle_connections_limit': 'server.server.idle.connections.limit',
    'haproxy_server_idle_connections_limit': 'server.idle.connections.limit',  # rename since >= 2.3
    'haproxy_server_internal_errors_total': 'server.internal.errors.total',
    'haproxy_server_last_session_seconds': 'server.last.session.seconds',
    'haproxy_server_limit_sessions': 'server.limit.sessions',
    'haproxy_server_loadbalanced_total': 'server.loadbalanced.total',
    'haproxy_server_max_connect_time_seconds': 'server.max.connect.time.seconds',
    'haproxy_server_max_queue': 'server.max.queue',
    'haproxy_server_max_queue_time_seconds': 'server.max.queue.time.seconds',
    'haproxy_server_max_response_time_seconds': 'server.max.response.time.seconds',
    'haproxy_server_max_session_rate': 'server.max.session.rate',
    'haproxy_server_max_sessions': 'server.max.sessions',
    'haproxy_server_max_total_time_seconds': 'server.max.total.time.seconds',
    'haproxy_server_need_connections_current': 'server.need.connections.current',
    'haproxy_server_queue_limit': 'server.queue.limit',
    'haproxy_server_queue_time_average_seconds': 'server.queue.time.average.seconds',
    'haproxy_server_redispatch_warnings_total': 'server.redispatch.warnings.total',
    'haproxy_server_response_errors_total': 'server.response.errors.total',
    'haproxy_server_responses_denied_total': 'server.responses.denied.total',
    'haproxy_server_response_time_average_seconds': 'server.response.time.average.seconds',
    'haproxy_server_retry_warnings_total': 'server.retry.warnings.total',
    'haproxy_server_safe_idle_connections_current': 'server.safe.idle.connections.current',
    'haproxy_server_server_aborts_total': 'server.server.aborts.total',
    'haproxy_server_sessions_total': 'server.sessions.total',
    'haproxy_server_status': 'server.status',
    'haproxy_server_total_time_average_seconds': 'server.total.time.average.seconds',
    'haproxy_server_unsafe_idle_connections_current': 'server.unsafe.idle.connections.current',
    'haproxy_server_used_connections_current': 'server.used.connections.current',
    'haproxy_server_uweight': 'server.uweight',
    'haproxy_server_weight': 'server.weight',
    'haproxy_sticktable_size': 'sticktable.size',
    'haproxy_sticktable_used': 'sticktable.used',
}
