#******************************************************************************
#*
#*  Copyright (C) 2009-2012 Broadcom Corporation
#*
#*  Licensed under the Apache License, Version 2.0 (the "License");
#*  you may not use this file except in compliance with the License.
#*  You may obtain a copy of the License at
#*
#*      http://www.apache.org/licenses/LICENSE-2.0
#*
#*  Unless required by applicable law or agreed to in writing, software
#*  distributed under the License is distributed on an "AS IS" BASIS,
#*  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#*  See the License for the specific language governing permissions and
#*  limitations under the License.
#*
#******************************************************************************

LDLIBS = -lbluetooth
# CFLAGS=-g

CFLAGS=

all : brcm_patchram_plus brcm_patchram_plus_h5 brcm_patchram_plus_usb

brcm_patchram_plus_h5 : brcm_patchram_plus_h5.o

brcm_patchram_plus : brcm_patchram_plus.o

brcm_patchram_plus_usb : brcm_patchram_plus_usb.o

install:
	mkdir -p $(DESTDIR)/usr/sbin
	install brcm_patchram_plus $(DESTDIR)/usr/sbin
	install brcm_patchram_plus_h5 $(DESTDIR)/usr/sbin
	install brcm_patchram_plus_usb $(DESTDIR)/usr/sbin
