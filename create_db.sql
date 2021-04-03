-- -----------------------------------------------------
-- Table route
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS route(
  route_id TEXT PRIMARY KEY,
  station_code TEXT DEFAULT NULL,
  date_YYYY_MM_DD TEXT DEFAULT NULL,
  departure_time_utc TEXT DEFAULT NULL,
  executor_capacity_cm3 REAL DEFAULT NULL,
  route_score TEXT DEFAULT NULL);

CREATE INDEX IF NOT EXISTS  route_id_UNIQUE ON route (route_id ASC);
CREATE INDEX  IF NOT EXISTS station_index ON route (station_code ASC);
CREATE INDEX  IF NOT EXISTS date_index ON route (date_YYYY_MM_DD ASC);
CREATE INDEX  IF NOT EXISTS departure_time_index ON route (departure_time_utc ASC);
CREATE INDEX  IF NOT EXISTS route_score_index ON route (route_score ASC);


-- -----------------------------------------------------
-- Table route_path
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS route_path (
  index0 INTEGER PRIMARY KEY,
  stop_name TEXT DEFAULT NULL,
  lat REAL DEFAULT NULL,
  lng REAL DEFAULT NULL,
  route_id TEXT DEFAULT NULL,
  type TEXT DEFAULT NULL,
  zone_id TEXT DEFAULT NULL,
  actual INTEGER DEFAULT NULL,
  FOREIGN KEY (route_id)
    REFERENCES route (route_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
CREATE INDEX IF NOT EXISTS route_id_index ON route_path (route_id ASC);
CREATE INDEX IF NOT EXISTS stop_name_index ON route_path (stop_name ASC);
CREATE INDEX IF NOT EXISTS lat_index ON route_path (lat ASC);
CREATE INDEX IF NOT EXISTS lng_index ON route_path (lng ASC);
CREATE INDEX IF NOT EXISTS latlng_index ON route_path (lat ASC, lng ASC);
CREATE INDEX IF NOT EXISTS type_index ON route_path (type ASC);
CREATE INDEX IF NOT EXISTS actual_index ON route_path (actual ASC);


-- -----------------------------------------------------
-- Table package_data
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS package (
  index0 INTEGER PRIMARY KEY,
  route_id TEXT DEFAULT NULL,
  stop_name TEXT DEFAULT NULL,
  package_id TEXT DEFAULT NULL,
  scan_status TEXT DEFAULT NULL,
  time_window_start TEXT DEFAULT NULL,
  time_window_end TEXT DEFAULT NULL,
  planned_service_time_seconds INTEGER DEFAULT NULL,
  depth_cm REAL DEFAULT NULL,
  height_cm REAL DEFAULT NULL,
  width_cm REAL DEFAULT NULL,
  FOREIGN KEY (route_id)
    REFERENCES route_path (route_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  FOREIGN KEY (stop_name)
    REFERENCES route_path (stop_name)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
CREATE INDEX IF NOT EXISTS route_id_index ON package (route_id ASC) ;
CREATE INDEX IF NOT EXISTS package_id_index ON package (package_id ASC) ;
CREATE INDEX IF NOT EXISTS stop_index ON package (stop_name ASC) ;
CREATE INDEX IF NOT EXISTS timewindow_start_index ON package (time_window_start ASC) ;
CREATE INDEX IF NOT EXISTS timewindow_end_index ON package (time_window_end ASC) ;

-- -----------------------------------------------------
-- Table travel_times
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS travel_times (
  index0 INTEGER PRIMARY KEY,
  route_id TEXT DEFAULT NULL,
  stop1 TEXT DEFAULT NULL,
  stop2 TEXT DEFAULT NULL,
  travel_time REAL DEFAULT NULL,
  FOREIGN KEY (route_id)
    REFERENCES route (route_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  FOREIGN KEY (stop1)
    REFERENCES route_path (stop_name)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  FOREIGN KEY (stop2)
    REFERENCES route_path (stop_name)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
CREATE INDEX IF NOT EXISTS route_id_index ON travel_times (route_id ASC);
CREATE INDEX IF NOT EXISTS stop1_index ON travel_times (stop1 ASC);
CREATE INDEX IF NOT EXISTS stop2_index ON travel_times (stop2 ASC);