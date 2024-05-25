#!/bin/bash
set -e

pacman -Syu --noconfirm
pacman -S --noconfirm git wget curl nano vim python python-pip sudo

pacman -S --noconfirm nmap rustscan

echo "OSINT setup on Arch Linux completed."

exec "bash"