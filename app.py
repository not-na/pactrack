#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pactrack
#
#  Copyright 2019 notna <notna@apparat.org>
#
#  This file is part of pactrack.
#
#  pactrack is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  pactrack is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with pactrack.  If not, see <http://www.gnu.org/licenses/>.
#

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
