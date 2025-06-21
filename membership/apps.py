from django.apps import AppConfig
import logging


logger = logging.getLogger(__name__)
class MembershipConfig(AppConfig):
    """
    Creates the configuration for the memberhsip app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'membership'

    # This function causes a warning in the console
    # Measures have been taken to stop the function querying
    # the database before app configuration however django
    # will continue to prompt the warning as it does not know 
    # that the querying is now done after app configuration
    # The warnings can be ignored
    def ready(self):
        """
        This runs on the initialization of the :membership: app

        If the server is running, this function schedules a task 
        to be run at 00:00 each day
        
        """
        from apscheduler.schedulers.background import BackgroundScheduler
        from apscheduler.triggers.cron import CronTrigger
        from django_apscheduler.jobstores import DjangoJobStore
        # Importing the task
        from .tasks import update_membership_status

        scheduler = BackgroundScheduler()
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # Sets this task to run at 00:00-midnight every day
        # This calls the update_membership_status from membership.tasks
        scheduler.add_job(
            update_membership_status,
            trigger=CronTrigger(hour=0, minute=0),
            id="update_membership_status",  # unique id
            replace_existing=True,
        )
        scheduler.start()
        logger.info("Scheduler started!")