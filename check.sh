!/bin/bash

read lower_port upper_port < /proc/sys/net/ipv4/ip_local_port_range
for (( port = lower_port ; port <= upper_port ; port++)); do
    res="$(lsof -i -P -n | grep LISTEN | awk '{ print $9 }' | grep $port)"

    if [ -z "$res" ]; then
        break
    fi
done

echo "$port"
