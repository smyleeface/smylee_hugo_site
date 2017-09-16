+++
title = "Notes from September Projects"
date = "2016-09-30T17:00:00-08:00"
toc = false
draft = false
categories = ["Coding"]
tags = ["Debian", "nginx proxy", "Postgres", "saltstack"]
thumbnail = "/images/201609/note_cover.png"
+++

Worked on an odoo setup in saltstack in September. It runs on Debian and Prostgres both of which I've never used before. It's not difficult to find what you're looking for if you know the equivalent in it's respective program. These are my notes on the things I learned. Some of it might not make sense out of context.

## Redirect a domain locally

https://gist.github.com/soheilhy/8b94347ff8336d971ad0#step-9-optional----redirecting-based-on-host-name

* on local machine (mac) edit `sudo nano /etc/hosts`
* add the the domain name(s) to the localhost ip

```
127.0.0.1   localhost   www.example.com    example.com    my.special.domain.name
```

----------

## nginx Proxy:
In the nginx conf:

```
upstream example.com.upstream {
    server 127.0.0.1:8069;
}

server {
    listen 80;
    server_name   example.com   www.example.com;
    proxy_pass http://example.com.upstream;
}
```

----------

## Postgres commands

```
sudo -u odoo psql    ==    sudo mysql -u odoo

\list    ==    show databases;

\command <tablename>    ==    use database_name;

\dt+    ==    show tables;
```

----------

## Debian:

To install a deb file, put `.deb` files `/var/cache/apt/archives/` and install with `sudo dpkg -i /path/to.deb`.

### Add a daemon:
http://blog.terminal.com/using-daemon-to-daemonize-your-programs/

### See if daemon is running:
`ps -ef | grep odoo`

### Terminate daemon:
`sudo kill <pid>`

### Add the service:

`sudo vi /etc/init.d/<service_name>` (use template)
test using `sudo /etc/init.d/<service_name> start`

`sudo update-rc.d <service_name> defaults` (to add to list of services)
test using `sudo <service_name> start`

---------

## Sublime text:
Select a word and replace in the entire page:

  - [Command+D]x2+
  - Start typing, it should replace
  - Esc when finished

---------

## Salt-stack custom states:

* write python file that will evaluate or do something and return a true or false value.
* The filename of the state is the state name. The def function is the function name.
* It can be called:
```
id_of_state:
	- name_of_state_file.function_def
```
or can be used in an unless/onlyif
```
{{ project_shortname }}_add_odoo_launch_daemon:
	cmd.run:
	.
	.
	.
	- unless: name_of_state_file.function_def #returns True or False
```
* salt-call --local saltutil.sync_all (includes it in the stack when debugging)

---------

## How bash and sh are differet:

http://stackoverflow.com/questions/7369145/activating-a-virtualenv-using-a-shell-script-doesnt-seem-to-work

