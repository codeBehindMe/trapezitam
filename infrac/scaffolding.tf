/*
    trapezitam
    Copyright (C) 2019  aarontillekeratne

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Pudlic License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

/* adga
  Author: aarontillekeratne
  Contact: github.com/codeBehindMe
*/

terraform {

}
data "terraform_remote_state" "gcsbackenddef" {
  backend = "gcs"
  config {
    bucket = "${var.projectid}-tfstate"
  }
}