----------------------------------------------------------------------------------
-- BASIC ANALYSIS

-- TOTAL NUMBER OF BOOKINGS
SELECT COUNT(*) as TOTAL_RECORDS FROM ride_cancel;
-- BOOKINGS BY BOOKING STATUS
SELECT booking_status,COUNT(*) as distribution FROM ride_cancel
GROUP BY booking_status;
-- TOTAL REVENUE GENERATED FROM COMPLETED RIDES
SELECT SUM(booking_value) as revenue FROM ride_cancel;
-- AVERAGE BOOKING VALUE
SELECT ROUND(AVG(booking_value),2) as avg_amount FROM ride_cancel;
-- AVERAGE RIDE DISTANCE
SELECT ROUND(AVG(ride_distance),2) as avg_distance FROM ride_cancel;
---------------------------------------------------------------------------------
-- VEHICLE ANALYSIS

-- TOTAL BOOKING BY VEHICLE TYPE
SELECT vehicle_type,COUNT(*) as distribution FROM ride_cancel
GROUP BY vehicle_type;
-- CANCELLATION RATE BY VEHICLE TYPE
SELECT vehicle_type,COUNT(*)*100/(SELECT COUNT(*) FROM ride_cancel WHERE incomplete_rides = 1.0)
AS vehicle_cancel_percent FROM ride_cancel
WHERE incomplete_rides = 1.0
GROUP BY vehicle_type;
-- AVERAGE BOOKING VALUE BY VEHICLE TYPE
SELECT vehicle_type,ROUND(AVG(booking_value),2) as AVG_AMOUNT FROM ride_cancel
GROUP BY vehicle_type;
-- AVERAGE RIDE DISTANCE BY VEHICLE TYPE
SELECT vehicle_type,ROUND(AVG(ride_distance),2) as AVG_DISTANCE FROM ride_cancel
GROUP BY vehicle_type;
-----------------------------------------------------------------------------------
-- TIME-BASED ANALYSIS

-- TOTAL BOOKINGS BY HOUR OF DAY
SELECT EXTRACT(HOUR FROM time) as hour,COUNT(*) as TOTAL_BOOKING FROM ride_cancel
GROUP BY hour ORDER BY hour;
-- CANCELLATION RATE BY HOUR OF THE DAY
SELECT EXTRACT(HOUR FROM time) as hour, COUNT(*)*100/(SELECT COUNT(*) FROM ride_cancel 
WHERE incomplete_rides = 1.0) AS cancel_rate_by_hour FROM ride_cancel
WHERE incomplete_rides = 1.0
GROUP BY hour ORDER BY hour;
-- TOTAL BOOKINGS BY DAY OF THE WEEK
SELECT EXTRACT(DAY FROM date) as DAY,COUNT(*) as total_bookings FROM ride_cancel
GROUP BY DAY;
-- PEAK BOOKINGS HOURS
SELECT EXTRACT(HOUR FROM time) as HOUR,COUNT(*) as booking_count FROM ride_cancel
GROUP BY HOUR ORDER BY booking_count desc limit 5;
-----------------------------------------------------------------------------------
-- LOCATION ANALYSIS

-- TOP 10 PICKUP LOCATIONS BY BOOKINGS
SELECT pickup_location,COUNT(*) as total_booking FROM ride_cancel
GROUP BY pickup_location
ORDER BY total_booking desc limit 10;
-- TOP 10 DROP LOCATIONS BY BOOKINGS
SELECT drop_location,COUNT(*) as total_booking FROM ride_cancel
GROUP BY drop_location
ORDER BY total_booking desc limit 10;
-- PICKUP LOCATIONS WITH THE HIGHEST CANCELLATION RATE
SELECT pickup_location,COUNT(*)*100.0/(SELECT COUNT(*) FROM ride_cancel
WHERE incomplete_rides = 1.0) as incomplete_rate FROM ride_cancel
WHERE incomplete_rides = 1.0
GROUP BY pickup_location ORDER by incomplete_rate desc limit 1;
-------------------------------------------------------------------------
-- CUSTOMER & DRIVER ANALYSIS

-- AVERAGE CUSTOMER RATING FOR COMPLETED RIDES BY VEHICLE TYPE
SELECT vehicle_type,ROUND(AVG(customer_rating),2) as avg_customer_rating 
FROM ride_cancel
WHERE incomplete_rides = 0.0 AND customer_rating IS NOT NULL
GROUP BY vehicle_type;
-- AVERAGE DRIVER RATING FOR COMPLETED RIDES BY VEHICLE TYPE
SELECT vehicle_type,ROUND(AVG(driver_ratings),2)as avg_driver_rating 
FROM ride_cancel
WHERE incomplete_rides = 0.0 AND driver_ratings IS NOT NULL
GROUP BY vehicle_type;
-------------------------------------------------------------------------
-- BUSINESS INSIGHTS

-- BOOKING DISTRIBUTION BY PAYMENT METHOD
SELECT payment_method,COUNT(*) as distribution FROM ride_cancel
GROUP BY payment_method
ORDER BY distribution;
-- 7.Top 10 highest revenue pickup locations
SELECT pickup_location,SUM(booking_value) as location_revenue FROM ride_cancel
GROUP BY pickup_location
ORDER BY location_revenue desc limit 10;