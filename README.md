# check_is_openvpnCli_available

This simple script is needed to run it on the cron (default every 5 minutes).
The task of the script is to restart the systemD service, inside which the OpenVPN client is running. If the script logic determines that there is no ping to the OpenVPN server address three times in a row, then this is the reason to restart the OpenVPN client to restore the correct operation of the vpn.

Данный незатейливый скрипт нужен для его запуска по крону (дефолт каждые 5 минут).
Задача скрипта - перезапуск сервиса систем, внутри которого работает клиент openVpn. Если логикой скрипта будет установлено отсутствие пинга в адрес сервера openVpn три раза подряд, то это причина перезапускать клиента openVpn для восстановления корректной работы vpn.
