#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseModelImpl(object):
    def __init__(self, pk_id, name):
        self._pk_id = pk_id
        self._name = name

    @property
    def pk_id(self):
        return self._pk_id

    @property
    def name(self):
        return self._name

    @classmethod
    def table(cls):
        return cls.__name__

    def __repr__(self):
        return "{}.{}".format(self.pk_id, self.name)


class Resource(BaseModelImpl):
    pass


class Action(BaseModelImpl):
    pass


class Domain(BaseModelImpl):
    pass


class CredentialType(BaseModelImpl):
    pass


class Role(BaseModelImpl):
    def __init__(self, pk_id, name, permissions):
        super(Role, self).__init__(pk_id, name)
        self._permissions = permissions

    @property
    def permissions(self):
        """
        permissions associated with this role
        :return:
        """
        return self._permissions


class User(BaseModelImpl):
    def __init__(self, pk_id, name, **kwargs):
        super(User, self).__init__(pk_id, name)
        self._profile = kwargs

    @property
    def identifier(self):
        """
        identifier of this user
        :return:
        """
        return self.pk_id

    @property
    def account_lock_millis(self):
        """
        locked milliseconds of this user
        :return:
        """
        if 'account_lock_millis' in self._profile:
            return self._profile['account_lock_millis']
        else:
            return 0

    @property
    def phone_number(self):
        """
        phone number of this user
        :return:
        """
        if 'phone_number' in self._profile:
            return self._profile['phone_number']
        else:
            return ''

    @property
    def roles(self):
        """
        roles associated with this user
        :return:
        """
        if 'roles' in self._profile:
            return self._profile['roles']
        else:
            return []

    @roles.setter
    def roles(self, v):
        self._profile['roles'] = v

    @property
    def permissions(self):
        """
        permissions associated with this user
        :return:
        """
        if 'permissions' in self._profile:
            return self._profile['permissions']
        else:
            return []

    @permissions.setter
    def permissions(self, v):
        self._profile['permissions'] = v


class Permission(BaseModelImpl):
    def __init__(self, pk_id, name, **kwargs):
        super(Permission, self).__init__(pk_id, name)
        self._profile = kwargs

    @property
    def domain_id(self):
        """
        domain id of the permission
        :return:
        """
        if 'domain_id' in self._profile:
            return self._profile['domain_id']
        else:
            return ''

    @property
    def action_id(self):
        """
        action id of the permission
        :return:
        """
        if 'action_id' in self._profile:
            return self._profile['action_id']
        else:
            return ''

    @property
    def resource_id(self):
        """
        resource id of the permission
        :return:
        """
        if 'resource_id' in self._profile:
            return self._profile['resource_id']
        else:
            return ''

    @property
    def roles(self):
        """
        roles associated with this permission
        :return:
        """
        if 'roles' in self._profile:
            return self._profile['roles']
        else:
            return ''

    @roles.setter
    def roles(self, v):
        self._profile['roles'] = v

    @property
    def users(self):
        """
        users associated with this permission
        :return:
        """
        if 'users' in self._profile:
            return self._profile['users']
        else:
            return ''

    @users.setter
    def users(self, v):
        self._profile['users'] = v


class Credential(BaseModelImpl):
    def __init__(self, pk_id, name, **kwargs):
        super(Credential, self).__init__(pk_id, name)
        self._profile = kwargs

    @property
    def user_id(self):
        """
        user_id associated with this Credential
        :return:
        """
        if 'user_id' in self._profile:
            return self._profile['user_id']
        else:
            return ''

    @property
    def credential(self):
        """
        credential associated with this Credential
        :return:
        """
        if 'credential' in self._profile:
            return self._profile['credential']
        else:
            return ''

    @property
    def credential_type(self):
        """
        credential type associated with this Credential
        :return:
        """
        if 'credential_type' in self._profile:
            return self._profile['credential_type']
        else:
            return ''

    @property
    def expiration_dt(self):
        """
        expiration_dt associated with this Credential
        :return:
        """
        if 'expiration_dt' in self._profile:
            return self._profile['expiration_dt']
        else:
            return ''

    @property
    def user(self):
        """
        user associated with this permission
        :return:
        """
        if 'user' in self._profile:
            return self._profile['user']
        else:
            return ''

    @user.setter
    def user(self, v):
        """
        :return:
        """
        self._profile['user'] = v
