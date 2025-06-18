from django.apps import AppConfig
import logging


logger = logging.getLogger(__name__)
class MembershipConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'membership'

    # This function causes a warning in the console
    # Measures have been taken to stop the function querying
    # the database before app configuration however django
    # will continue to prompt the warning as it does not know 
    # that the querying is now done after app configuration
    # The warnings can be ignored
    def ready(self):
        from apscheduler.schedulers.background import BackgroundScheduler
        from apscheduler.triggers.cron import CronTrigger
        from django_apscheduler.jobstores import DjangoJobStore
        # Importing the task
        from .tasks import update_membership_status

        scheduler = BackgroundScheduler()
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # Run this task at 00 every day
        scheduler.add_job(
            update_membership_status,
            trigger=CronTrigger(hour=0, minute=0),
            id="update_membership_status",  # unique id
            replace_existing=True,
        )
        scheduler.start()
        logger.info("Scheduler started!")