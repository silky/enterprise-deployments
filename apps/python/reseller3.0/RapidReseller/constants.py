#!/usr/bin/python
#
# Copyright 2013 Google Inc. All Rights Reserved.

__author__ = 'richieforeman@google.com (Richie Foreman)'


class ResellerProduct(object):
  GoogleApps = "Google-Apps"
  GoogleDrive = "Google-Drive-storage"
  GoogleVault = "Google-Vault"


class ResellerSKU(object):
  '''
  A class of constants containing various Enterprise SKUs.

  src: https://developers.google.com/admin-sdk/reseller/v1/how-tos/products
  '''

  GoogleApps = "Google-Apps-For-Business"
  GoogleDriveStorage20GB = "Google-Drive-storage-20GB"
  GoogleDriveStorage50GB = "Google-Drive-storage-50GB"
  GoogleDriveStorage200GB = "Google-Drive-storage-200GB"
  GoogleDriveStorage400GB = "Google-Drive-storage-400GB"
  GoogleDriveStorage1TB = "Google-Drive-storage-1TB"
  GoogleDriveStorage2TB = "Google-Drive-storage-2TB"
  GoogleDriveStorage4TB = "Google-Drive-storage-4TB"
  GoogleDriveStorage8TB = "Google-Drive-storage-8TB"
  GoogleDriveStorage16TB = "Google-Drive-storage-16TB"
  GoogleVault = "Google-Vault"


class ResellerPlanName(object):
  # Annual Prepaid for the entire year.
  AnnualYearly = "ANNUAL_YEARLY_PAY"

  # Annual paid every month.
  AnnualMonthly = "ANNUAL_MONTHLY_PAY"

  # Month-to-Month
  Flexible = "FLEXIBLE"

  # 30 Day (max) trial.
  Trial = "TRIAL"


class ResellerDeletionType(object):
  Cancel = "cancel"
  Downgrade = "downgrade"
  Suspend = "suspend"


class ResellerRenewalType(object):
  # Auto renew with monthly pay
  AutoRenewMonthly = "AUTO_RENEW_MONTHLY_PAY"

  # auto renew with yearly pay
  AutoRenewYearly = "AUTO_RENEW_YEARLY_PAY"

  # renew current users with monthly pay
  RenewCurrentUsersMonthly = "RENEW_CURRENT_USERS_MONTHLY_PAY"

  # renew current users with yearly pay.
  RenewCurrentUsersYearly = "RENEW_CURRENT_USERS_YEARLY_PAY"

  # at the renewal date, switch to a "FLEXIBLE" plan type,
  # which is billed on a monthly basis.
  PayAsYouGo = "SWITCH_TO_PAY_AS_YOU_GO"

  # at the renewal date, cancel the subscription
  Cancel = "CANCEL"