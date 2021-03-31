import React, { useState, Fragment } from 'react';
import { LatLngExpression } from 'leaflet';
import { Marker, Popup, Polyline } from 'react-leaflet';

import { useRoutes } from '../hooks/api-hooks';
import Map from '../../common/map/Map';
import { Stop } from '../stops/Stops';
import styles from './routes.module.css';

type Route = {
  id: number;
  name: string;
  stops: Stop[];
};

const Routes = () => {
  const [params, setParams] = useState<string>('');
  const { data, refetch } = useRoutes(params);

  const search = (e: React.SyntheticEvent) => {
    e.preventDefault();
    const target = e.target as typeof e.target & {
      stopId: { value: string };
    };
    const stopId = target.stopId.value;
    const params = `?stop_id=${stopId}`;
    setParams(params);
    setTimeout(() => {
      refetch();
    }, 200);
  };

  const drawLine = (stops: Stop[]): LatLngExpression[] => {
    return stops.map((stop: Stop) => {
      return [stop.coordinates.latitude, stop.coordinates.longitude];
    });
  };

  return (
    <>
      <h1>Routes</h1>
      <form onSubmit={search} className={styles.form}>
        <label htmlFor="stopId">Stop id</label>
        <input name="stopId" className={styles.input} />
        <button type="submit">Search</button>
      </form>
      <Map>
        {data?.map((route: Route) => (
          <Fragment key={route.name + route.id}>
            {route?.stops?.map((stop: Stop) => (
              <Marker
                key={stop.id}
                position={[
                  stop.coordinates.latitude,
                  stop.coordinates.longitude,
                ]}
              >
                <Popup>
                  <p>{stop.id}</p>
                  <p>{stop.name}</p>
                </Popup>
              </Marker>
            ))}
            <Polyline positions={drawLine(route?.stops)} />
          </Fragment>
        ))}
      </Map>
    </>
  );
};

export default Routes;
