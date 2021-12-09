Module(
    body=[
        Expr(
            value=Constant(value='The Odoo API module defines Odoo Environments and method decorators.\n\n.. todo:: Document this module\n', kind=None),
        ),
        Assign(
            targets=[Name(id='__all__', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='Environment', kind=None),
                    Constant(value='Meta', kind=None),
                    Constant(value='model', kind=None),
                    Constant(value='constrains', kind=None),
                    Constant(value='depends', kind=None),
                    Constant(value='onchange', kind=None),
                    Constant(value='returns', kind=None),
                    Constant(value='call_kw', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='warnings', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='collections.abc',
            names=[alias(name='Mapping', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='contextlib',
            names=[alias(name='contextmanager', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='inspect',
            names=[alias(name='signature', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='pprint',
            names=[alias(name='pformat', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='weakref',
            names=[alias(name='WeakSet', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='decorator',
            names=[alias(name='decorate', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='exceptions',
            names=[alias(name='CacheMiss', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='tools',
            names=[
                alias(name='frozendict', asname=None),
                alias(name='classproperty', asname=None),
                alias(name='lazy_property', asname=None),
                alias(name='StackMap', asname=None),
            ],
            level=1,
        ),
        ImportFrom(
            module='tools.translate',
            names=[alias(name='_', asname=None)],
            level=1,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='INHERITED_ATTRS', ctx=Store())],
            value=Tuple(
                elts=[Constant(value='_returns', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='Params',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                            arg(arg='kwargs', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='args',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='args', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='kwargs',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='kwargs', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__str__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='arg', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='args',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='params', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='repr', ctx=Load()),
                                                args=[Name(id='arg', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='item', ctx=Store()),
                            iter=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='kwargs',
                                                ctx=Load(),
                                            ),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='params', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s=%r', kind=None),
                                                op=Mod(),
                                                right=Name(id='item', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=', ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='params', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='Meta',
            bases=[Name(id='type', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Metaclass that automatically decorates traditional-style methods by\n        guessing their API. It also implements the inheritance of the\n        :func:`returns` decorators.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__new__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='meta', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='bases', annotation=None, type_comment=None),
                            arg(arg='attrs', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='parent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='type', ctx=Load()),
                                    attr='__new__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='meta', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Name(id='bases', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='attrs', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='key', ctx=Load()),
                                                        attr='startswith',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='__', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Call(
                                                func=Name(id='callable', ctx=Load()),
                                                args=[Name(id='value', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=Call(
                                                func=Name(id='propagate', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='getattr', ctx=Load()),
                                                        args=[
                                                            Name(id='parent', ctx=Load()),
                                                            Name(id='key', ctx=Load()),
                                                            Constant(value=None, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Name(id='value', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Call(
                                                                func=Name(id='getattr', ctx=Load()),
                                                                args=[
                                                                    Name(id='value', ctx=Load()),
                                                                    Constant(value='_api', kind=None),
                                                                    Constant(value=None, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='cr', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Deprecated method %s.%s in module %s', kind=None),
                                                            Name(id='name', ctx=Load()),
                                                            Name(id='key', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='attrs', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='__module__', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='attrs', ctx=Load()),
                                                    slice=Name(id='key', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='value', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='type', ctx=Load()),
                                    attr='__new__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='meta', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Name(id='bases', ctx=Load()),
                                    Name(id='attrs', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='attrsetter',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='attr', annotation=None, type_comment=None),
                    arg(arg='value', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a function that sets ``attr`` on its argument and returns it. ', kind=None),
                ),
                Return(
                    value=Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='method', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=BoolOp(
                            op=Or(),
                            values=[
                                Call(
                                    func=Name(id='setattr', ctx=Load()),
                                    args=[
                                        Name(id='method', ctx=Load()),
                                        Name(id='attr', ctx=Load()),
                                        Name(id='value', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                Name(id='method', ctx=Load()),
                            ],
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='propagate',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='method1', annotation=None, type_comment=None),
                    arg(arg='method2', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Propagate decorators from ``method1`` to ``method2``, and return the\n        resulting method.\n    ', kind=None),
                ),
                If(
                    test=Name(id='method1', ctx=Load()),
                    body=[
                        For(
                            target=Name(id='attr', ctx=Store()),
                            iter=Name(id='INHERITED_ATTRS', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id='hasattr', ctx=Load()),
                                                args=[
                                                    Name(id='method1', ctx=Load()),
                                                    Name(id='attr', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='hasattr', ctx=Load()),
                                                    args=[
                                                        Name(id='method2', ctx=Load()),
                                                        Name(id='attr', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='setattr', ctx=Load()),
                                                args=[
                                                    Name(id='method2', ctx=Load()),
                                                    Name(id='attr', ctx=Load()),
                                                    Call(
                                                        func=Name(id='getattr', ctx=Load()),
                                                        args=[
                                                            Name(id='method1', ctx=Load()),
                                                            Name(id='attr', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='method2', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='constrains',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Decorate a constraint checker.\n\n    Each argument must be a field name used in the check::\n\n        @api.constrains(\'name\', \'description\')\n        def _check_description(self):\n            for record in self:\n                if record.name == record.description:\n                    raise ValidationError("Fields name and description must be different")\n\n    Invoked on the records on which one of the named fields has been modified.\n\n    Should raise :exc:`~odoo.exceptions.ValidationError` if the\n    validation failed.\n\n    .. warning::\n\n        ``@constrains`` only supports simple field names, dotted names\n        (fields of relational fields e.g. ``partner_id.customer``) are not\n        supported and will be ignored.\n\n        ``@constrains`` will be triggered only if the declared fields in the\n        decorated method are included in the ``create`` or ``write`` call.\n        It implies that fields not present in a view will not trigger a call\n        during a record creation. A override of ``create`` is necessary to make\n        sure a constraint will always be triggered (e.g. to test the absence of\n        value).\n\n    One may also pass a single function as argument.  In that case, the field\n    names are given by calling the function with a model instance.\n\n    ', kind=None),
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='args', ctx=Load()),
                            Call(
                                func=Name(id='callable', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='args', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=Subscript(
                                value=Name(id='args', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Name(id='attrsetter', ctx=Load()),
                        args=[
                            Constant(value='_constrains', kind=None),
                            Name(id='args', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='ondelete',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=None,
                kwonlyargs=[arg(arg='at_uninstall', annotation=None, type_comment=None)],
                kw_defaults=[
                    None,
                ],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Mark a method to be executed during :meth:`~odoo.models.BaseModel.unlink`.\n\n    The goal of this decorator is to allow client-side errors when unlinking\n    records if, from a business point of view, it does not make sense to delete\n    such records. For instance, a user should not be able to delete a validated\n    sales order.\n\n    While this could be implemented by simply overriding the method ``unlink``\n    on the model, it has the drawback of not being compatible with module\n    uninstallation. When uninstalling the module, the override could raise user\n    errors, but we shouldn\'t care because the module is being uninstalled, and\n    thus **all** records related to the module should be removed anyway.\n\n    This means that by overriding ``unlink``, there is a big chance that some\n    tables/records may remain as leftover data from the uninstalled module. This\n    leaves the database in an inconsistent state. Moreover, there is a risk of\n    conflicts if the module is ever reinstalled on that database.\n\n    Methods decorated with ``@ondelete`` should raise an error following some\n    conditions, and by convention, the method should be named either\n    ``_unlink_if_<condition>`` or ``_unlink_except_<not_condition>``.\n\n    .. code-block:: python\n\n        @api.ondelete(at_uninstall=False)\n        def _unlink_if_user_inactive(self):\n            if any(user.active for user in self):\n                raise UserError("Can\'t delete an active user!")\n\n        # same as above but with _unlink_except_* as method name\n        @api.ondelete(at_uninstall=False)\n        def _unlink_except_active_user(self):\n            if any(user.active for user in self):\n                raise UserError("Can\'t delete an active user!")\n\n    :param bool at_uninstall: Whether the decorated method should be called if\n        the module that implements said method is being uninstalled. Should\n        almost always be ``False``, so that module uninstallation does not\n        trigger those errors.\n\n    .. danger::\n        The parameter ``at_uninstall`` should only be set to ``True`` if the\n        check you are implementing also applies when uninstalling the module.\n\n        For instance, it doesn\'t matter if when uninstalling ``sale``, validated\n        sales orders are being deleted because all data pertaining to ``sale``\n        should be deleted anyway, in that case ``at_uninstall`` should be set to\n        ``False``.\n\n        However, it makes sense to prevent the removal of the default language\n        if no other languages are installed, since deleting the default language\n        will break a lot of basic behavior. In this case, ``at_uninstall``\n        should be set to ``True``.\n    ', kind=None),
                ),
                Return(
                    value=Call(
                        func=Name(id='attrsetter', ctx=Load()),
                        args=[
                            Constant(value='_ondelete', kind=None),
                            Name(id='at_uninstall', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='onchange',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Return a decorator to decorate an onchange method for given fields.\n\n    In the form views where the field appears, the method will be called\n    when one of the given fields is modified. The method is invoked on a\n    pseudo-record that contains the values present in the form. Field\n    assignments on that record are automatically sent back to the client.\n\n    Each argument must be a field name::\n\n        @api.onchange(\'partner_id\')\n        def _onchange_partner(self):\n            self.message = "Dear %s" % (self.partner_id.name or "")\n\n    .. code-block:: python\n\n        return {\n            \'warning\': {\'title\': "Warning", \'message\': "What is this?", \'type\': \'notification\'},\n        }\n\n    If the type is set to notification, the warning will be displayed in a notification.\n    Otherwise it will be displayed in a dialog as default.\n\n    .. warning::\n\n        ``@onchange`` only supports simple field names, dotted names\n        (fields of relational fields e.g. ``partner_id.tz``) are not\n        supported and will be ignored\n\n    .. danger::\n\n        Since ``@onchange`` returns a recordset of pseudo-records,\n        calling any one of the CRUD methods\n        (:meth:`create`, :meth:`read`, :meth:`write`, :meth:`unlink`)\n        on the aforementioned recordset is undefined behaviour,\n        as they potentially do not exist in the database yet.\n\n        Instead, simply set the record\'s field like shown in the example\n        above or call the :meth:`update` method.\n\n    .. warning::\n\n        It is not possible for a ``one2many`` or ``many2many`` field to modify\n        itself via onchange. This is a webclient limitation - see `#2693 <https://github.com/odoo/odoo/issues/2693>`_.\n\n    ', kind=None),
                ),
                Return(
                    value=Call(
                        func=Name(id='attrsetter', ctx=Load()),
                        args=[
                            Constant(value='_onchange', kind=None),
                            Name(id='args', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='depends',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a decorator that specifies the field dependencies of a "compute"\n        method (for new-style function fields). Each argument must be a string\n        that consists in a dot-separated sequence of field names::\n\n            pname = fields.Char(compute=\'_compute_pname\')\n\n            @api.depends(\'partner_id.name\', \'partner_id.is_company\')\n            def _compute_pname(self):\n                for record in self:\n                    if record.partner_id.is_company:\n                        record.pname = (record.partner_id.name or "").upper()\n                    else:\n                        record.pname = record.partner_id.name\n\n        One may also pass a single function as argument. In that case, the\n        dependencies are given by calling the function with the field\'s model.\n    ', kind=None),
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='args', ctx=Load()),
                            Call(
                                func=Name(id='callable', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='args', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=Subscript(
                                value=Name(id='args', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Constant(value='id', kind=None),
                                            ops=[In()],
                                            comparators=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='arg', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='.', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='arg', ctx=Store()),
                                                iter=Name(id='args', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='NotImplementedError', ctx=Load()),
                                        args=[Constant(value="Compute method cannot depend on field 'id'.", kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                ),
                Return(
                    value=Call(
                        func=Name(id='attrsetter', ctx=Load()),
                        args=[
                            Constant(value='_depends', kind=None),
                            Name(id='args', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='depends_context',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a decorator that specifies the context dependencies of a\n    non-stored "compute" method.  Each argument is a key in the context\'s\n    dictionary::\n\n        price = fields.Float(compute=\'_compute_product_price\')\n\n        @api.depends_context(\'pricelist\')\n        def _compute_product_price(self):\n            for product in self:\n                if product.env.context.get(\'pricelist\'):\n                    pricelist = self.env[\'product.pricelist\'].browse(product.env.context[\'pricelist\'])\n                else:\n                    pricelist = self.env[\'product.pricelist\'].get_default_pricelist()\n                product.price = pricelist.get_products_price(product).get(product.id, 0.0)\n\n    All dependencies must be hashable.  The following keys have special\n    support:\n\n    * `company` (value in context or current company id),\n    * `uid` (current user id and superuser flag),\n    * `active_test` (value in env.context or value in field.context).\n    ', kind=None),
                ),
                Return(
                    value=Call(
                        func=Name(id='attrsetter', ctx=Load()),
                        args=[
                            Constant(value='_depends_context', kind=None),
                            Name(id='args', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='returns',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='model', annotation=None, type_comment=None),
                    arg(arg='downgrade', annotation=None, type_comment=None),
                    arg(arg='upgrade', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=" Return a decorator for methods that return instances of ``model``.\n\n        :param model: a model name, or ``'self'`` for the current model\n\n        :param downgrade: a function ``downgrade(self, value, *args, **kwargs)``\n            to convert the record-style ``value`` to a traditional-style output\n\n        :param upgrade: a function ``upgrade(self, value, *args, **kwargs)``\n            to convert the traditional-style ``value`` to a record-style output\n\n        The arguments ``self``, ``*args`` and ``**kwargs`` are the ones passed\n        to the method in the record-style.\n\n        The decorator adapts the method output to the api style: ``id``, ``ids`` or\n        ``False`` for the traditional style, and recordset for the record style::\n\n            @model\n            @returns('res.partner')\n            def find_partner(self, arg):\n                ...     # return some record\n\n            # output depends on call style: traditional vs record style\n            partner_id = model.find_partner(cr, uid, arg, context=context)\n\n            # recs = model.browse(cr, uid, ids, context)\n            partner_record = recs.find_partner(arg)\n\n        Note that the decorated method must satisfy that convention.\n\n        Those decorators are automatically *inherited*: a method that overrides\n        a decorated existing method will be decorated with the same\n        ``@returns(model)``.\n    ", kind=None),
                ),
                Return(
                    value=Call(
                        func=Name(id='attrsetter', ctx=Load()),
                        args=[
                            Constant(value='_returns', kind=None),
                            Tuple(
                                elts=[
                                    Name(id='model', ctx=Load()),
                                    Name(id='downgrade', ctx=Load()),
                                    Name(id='upgrade', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='downgrade',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='method', annotation=None, type_comment=None),
                    arg(arg='value', annotation=None, type_comment=None),
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='args', annotation=None, type_comment=None),
                    arg(arg='kwargs', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Convert ``value`` returned by ``method`` on ``self`` to traditional style. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='spec', ctx=Store())],
                    value=Call(
                        func=Name(id='getattr', ctx=Load()),
                        args=[
                            Name(id='method', ctx=Load()),
                            Constant(value='_returns', kind=None),
                            Constant(value=None, kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='spec', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Name(id='value', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='_', ctx=Store()),
                                Name(id='convert', ctx=Store()),
                                Name(id='_', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='spec', ctx=Load()),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='convert', ctx=Load()),
                            Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Call(
                                                func=Name(id='signature', ctx=Load()),
                                                args=[Name(id='convert', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='parameters',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='convert', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='value', ctx=Load()),
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[
                        If(
                            test=Name(id='convert', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='convert', ctx=Load()),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='split_context',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='method', annotation=None, type_comment=None),
                    arg(arg='args', annotation=None, type_comment=None),
                    arg(arg='kwargs', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Extract the context from a pair of positional and keyword arguments.\n        Return a triple ``context, args, kwargs``.\n    ', kind=None),
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='context', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            Name(id='args', ctx=Load()),
                            Name(id='kwargs', ctx=Load()),
                        ],
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='autovacuum',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='method', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Decorate a method so that it is called by the daily vacuum cron job (model\n    ``ir.autovacuum``).  This is typically used for garbage-collection-like\n    tasks that do not deserve a specific cron job.\n    ', kind=None),
                ),
                Assert(
                    test=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='method', ctx=Load()),
                                attr='__name__',
                                ctx=Load(),
                            ),
                            attr='startswith',
                            ctx=Load(),
                        ),
                        args=[Constant(value='_', kind=None)],
                        keywords=[],
                    ),
                    msg=BinOp(
                        left=Constant(value='%s: autovacuum methods must be private', kind=None),
                        op=Mod(),
                        right=Attribute(
                            value=Name(id='method', ctx=Load()),
                            attr='__name__',
                            ctx=Load(),
                        ),
                    ),
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='method', ctx=Load()),
                            attr='_autovacuum',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='method', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='model',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='method', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Decorate a record-style method where ``self`` is a recordset, but its\n        contents is not relevant, only the model is. Such a method::\n\n            @api.model\n            def method(self, args):\n                ...\n\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='method', ctx=Load()),
                            attr='__name__',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='create', kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='model_create_single', ctx=Load()),
                                args=[Name(id='method', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='method', ctx=Load()),
                            attr='_api',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(value='model', kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='method', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_create_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[
                    BinOp(
                        left=Name(id='__name__', ctx=Load()),
                        op=Add(),
                        right=Constant(value='.create', kind=None),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='_model_create_single',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='create', annotation=None, type_comment=None),
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='arg', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='arg', ctx=Load()),
                            Name(id='Mapping', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='create', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='arg', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='arg', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[Gt()],
                        comparators=[Constant(value=1, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_create_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%s.create() called with %d dicts', kind=None),
                                    Name(id='self', ctx=Load()),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='arg', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr='concat',
                            ctx=Load(),
                        ),
                        args=[
                            Starred(
                                value=GeneratorExp(
                                    elt=Call(
                                        func=Name(id='create', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Name(id='vals', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Name(id='vals', ctx=Store()),
                                            iter=Name(id='arg', ctx=Load()),
                                            ifs=[],
                                            is_async=0,
                                        ),
                                    ],
                                ),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='model_create_single',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='method', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Decorate a method that takes a dictionary and creates a single record.\n        The method may be called with either a single dict or a list of dicts::\n\n            record = model.create(vals)\n            records = model.create([vals, ...])\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='wrapper', ctx=Store())],
                    value=Call(
                        func=Name(id='decorate', ctx=Load()),
                        args=[
                            Name(id='method', ctx=Load()),
                            Name(id='_model_create_single', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='wrapper', ctx=Load()),
                            attr='_api',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(value='model_create', kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='wrapper', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_model_create_multi',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='create', annotation=None, type_comment=None),
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='arg', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='arg', ctx=Load()),
                            Name(id='Mapping', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='create', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    List(
                                        elts=[Name(id='arg', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Name(id='create', ctx=Load()),
                        args=[
                            Name(id='self', ctx=Load()),
                            Name(id='arg', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='model_create_multi',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='method', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Decorate a method that takes a list of dictionaries and creates multiple\n        records. The method may be called with either a single dict or a list of\n        dicts::\n\n            record = model.create(vals)\n            records = model.create([vals, ...])\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='wrapper', ctx=Store())],
                    value=Call(
                        func=Name(id='decorate', ctx=Load()),
                        args=[
                            Name(id='method', ctx=Load()),
                            Name(id='_model_create_multi', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='wrapper', ctx=Load()),
                            attr='_api',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(value='model_create', kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='wrapper', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_call_kw_model',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='method', annotation=None, type_comment=None),
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='args', annotation=None, type_comment=None),
                    arg(arg='kwargs', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='context', ctx=Store()),
                                Name(id='args', ctx=Store()),
                                Name(id='kwargs', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Name(id='split_context', ctx=Load()),
                        args=[
                            Name(id='method', ctx=Load()),
                            Name(id='args', ctx=Load()),
                            Name(id='kwargs', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='recs', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='self', ctx=Load()),
                            attr='with_context',
                            ctx=Load(),
                        ),
                        args=[
                            BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='context', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='call %s.%s(%s)', kind=None),
                            Name(id='recs', ctx=Load()),
                            Attribute(
                                value=Name(id='method', ctx=Load()),
                                attr='__name__',
                                ctx=Load(),
                            ),
                            Call(
                                func=Name(id='Params', ctx=Load()),
                                args=[
                                    Name(id='args', ctx=Load()),
                                    Name(id='kwargs', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=Call(
                        func=Name(id='method', ctx=Load()),
                        args=[
                            Name(id='recs', ctx=Load()),
                            Starred(
                                value=Name(id='args', ctx=Load()),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg=None,
                                value=Name(id='kwargs', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='downgrade', ctx=Load()),
                        args=[
                            Name(id='method', ctx=Load()),
                            Name(id='result', ctx=Load()),
                            Name(id='recs', ctx=Load()),
                            Name(id='args', ctx=Load()),
                            Name(id='kwargs', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_call_kw_model_create',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='method', annotation=None, type_comment=None),
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='args', annotation=None, type_comment=None),
                    arg(arg='kwargs', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='context', ctx=Store()),
                                Name(id='args', ctx=Store()),
                                Name(id='kwargs', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Name(id='split_context', ctx=Load()),
                        args=[
                            Name(id='method', ctx=Load()),
                            Name(id='args', ctx=Load()),
                            Name(id='kwargs', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='recs', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='self', ctx=Load()),
                            attr='with_context',
                            ctx=Load(),
                        ),
                        args=[
                            BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='context', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='call %s.%s(%s)', kind=None),
                            Name(id='recs', ctx=Load()),
                            Attribute(
                                value=Name(id='method', ctx=Load()),
                                attr='__name__',
                                ctx=Load(),
                            ),
                            Call(
                                func=Name(id='Params', ctx=Load()),
                                args=[
                                    Name(id='args', ctx=Load()),
                                    Name(id='kwargs', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=Call(
                        func=Name(id='method', ctx=Load()),
                        args=[
                            Name(id='recs', ctx=Load()),
                            Starred(
                                value=Name(id='args', ctx=Load()),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg=None,
                                value=Name(id='kwargs', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=IfExp(
                        test=Call(
                            func=Name(id='isinstance', ctx=Load()),
                            args=[
                                Subscript(
                                    value=Name(id='args', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                Name(id='Mapping', ctx=Load()),
                            ],
                            keywords=[],
                        ),
                        body=Attribute(
                            value=Name(id='result', ctx=Load()),
                            attr='id',
                            ctx=Load(),
                        ),
                        orelse=Attribute(
                            value=Name(id='result', ctx=Load()),
                            attr='ids',
                            ctx=Load(),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_call_kw_multi',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='method', annotation=None, type_comment=None),
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='args', annotation=None, type_comment=None),
                    arg(arg='kwargs', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='ids', ctx=Store()),
                                Name(id='args', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Tuple(
                        elts=[
                            Subscript(
                                value=Name(id='args', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            Subscript(
                                value=Name(id='args', ctx=Load()),
                                slice=Slice(
                                    lower=Constant(value=1, kind=None),
                                    upper=None,
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='context', ctx=Store()),
                                Name(id='args', ctx=Store()),
                                Name(id='kwargs', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Name(id='split_context', ctx=Load()),
                        args=[
                            Name(id='method', ctx=Load()),
                            Name(id='args', ctx=Load()),
                            Name(id='kwargs', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='recs', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='context', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            attr='browse',
                            ctx=Load(),
                        ),
                        args=[Name(id='ids', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='call %s.%s(%s)', kind=None),
                            Name(id='recs', ctx=Load()),
                            Attribute(
                                value=Name(id='method', ctx=Load()),
                                attr='__name__',
                                ctx=Load(),
                            ),
                            Call(
                                func=Name(id='Params', ctx=Load()),
                                args=[
                                    Name(id='args', ctx=Load()),
                                    Name(id='kwargs', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=Call(
                        func=Name(id='method', ctx=Load()),
                        args=[
                            Name(id='recs', ctx=Load()),
                            Starred(
                                value=Name(id='args', ctx=Load()),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg=None,
                                value=Name(id='kwargs', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='downgrade', ctx=Load()),
                        args=[
                            Name(id='method', ctx=Load()),
                            Name(id='result', ctx=Load()),
                            Name(id='recs', ctx=Load()),
                            Name(id='args', ctx=Load()),
                            Name(id='kwargs', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='call_kw',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='model', annotation=None, type_comment=None),
                    arg(arg='name', annotation=None, type_comment=None),
                    arg(arg='args', annotation=None, type_comment=None),
                    arg(arg='kwargs', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Invoke the given method ``name`` on the recordset ``model``. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='method', ctx=Store())],
                    value=Call(
                        func=Name(id='getattr', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='type', ctx=Load()),
                                args=[Name(id='model', ctx=Load())],
                                keywords=[],
                            ),
                            Name(id='name', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='api', ctx=Store())],
                    value=Call(
                        func=Name(id='getattr', ctx=Load()),
                        args=[
                            Name(id='method', ctx=Load()),
                            Constant(value='_api', kind=None),
                            Constant(value=None, kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='api', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='model', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='_call_kw_model', ctx=Load()),
                                args=[
                                    Name(id='method', ctx=Load()),
                                    Name(id='model', ctx=Load()),
                                    Name(id='args', ctx=Load()),
                                    Name(id='kwargs', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Name(id='api', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='model_create', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_call_kw_model_create', ctx=Load()),
                                        args=[
                                            Name(id='method', ctx=Load()),
                                            Name(id='model', ctx=Load()),
                                            Name(id='args', ctx=Load()),
                                            Name(id='kwargs', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_call_kw_multi', ctx=Load()),
                                        args=[
                                            Name(id='method', ctx=Load()),
                                            Name(id='model', ctx=Load()),
                                            Name(id='args', ctx=Load()),
                                            Name(id='kwargs', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='model', ctx=Load()),
                            attr='flush',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Name(id='result', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='Environment',
            bases=[Name(id='Mapping', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' An environment wraps data for ORM records:\n\n        - :attr:`cr`, the current database cursor;\n        - :attr:`uid`, the current user id;\n        - :attr:`context`, the current context dictionary;\n        - :attr:`su`, whether in superuser mode.\n\n        It provides access to the registry by implementing a mapping from model\n        names to new api models. It also holds a cache for records, and a data\n        structure to manage recomputations.\n    ', kind=None),
                ),
                FunctionDef(
                    name='envs',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[Constant(value='Since Odoo 15.0, Environment.envs no longer works; use cr.transaction or env.transaction instead.', kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[Name(id='classproperty', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='manage',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='warnings', ctx=Load()),
                                    attr='warn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Since Odoo 15.0, Environment.manage() is useless.', kind=None),
                                    Name(id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='stacklevel',
                                        value=Constant(value=2, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Yield(value=None),
                        ),
                    ],
                    decorator_list=[
                        Name(id='classmethod', ctx=Load()),
                        Name(id='contextmanager', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='reset',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Reset the transaction, see :meth:`Transaction.reset`. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='transaction',
                                        ctx=Load(),
                                    ),
                                    attr='reset',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__new__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='cr', annotation=None, type_comment=None),
                            arg(arg='uid', annotation=None, type_comment=None),
                            arg(arg='context', annotation=None, type_comment=None),
                            arg(arg='su', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='uid', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Name(id='SUPERUSER_ID', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='su', ctx=Store())],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assert(
                            test=Compare(
                                left=Name(id='context', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='uid', ctx=Load()),
                                    Name(id='context', ctx=Load()),
                                    Name(id='su', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='transaction', ctx=Store())],
                            value=Attribute(
                                value=Name(id='cr', ctx=Load()),
                                attr='transaction',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='env', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='transaction', ctx=Load()),
                                attr='envs',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='env', ctx=Load()),
                                            attr='args',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='args', ctx=Load())],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='env', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='self', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='object', ctx=Load()),
                                    attr='__new__',
                                    ctx=Load(),
                                ),
                                args=[Name(id='cls', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='uid', ctx=Load()),
                                    Call(
                                        func=Name(id='frozendict', ctx=Load()),
                                        args=[Name(id='context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='su', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='cr',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='uid',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='context',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='su',
                                            ctx=Store(),
                                        ),
                                    ],
                                    ctx=Store(),
                                ),
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='args',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='args', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='transaction',
                                    ctx=Store(),
                                ),
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='all',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='transaction', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='registry',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='transaction', ctx=Load()),
                                attr='registry',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='cache',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='transaction', ctx=Load()),
                                attr='cache',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_cache_key',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_protected',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='transaction', ctx=Load()),
                                attr='protected',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='transaction', ctx=Load()),
                                        attr='envs',
                                        ctx=Load(),
                                    ),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='self', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__contains__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Test whether the given model exists. ', kind=None),
                        ),
                        Return(
                            value=Compare(
                                left=Name(id='model_name', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__getitem__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return an empty recordset from the given model. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model_name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='_browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Tuple(elts=[], ctx=Load()),
                                    Tuple(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__iter__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return an iterator on model names. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='iter', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__len__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the size of the model registry. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__eq__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Compare(
                                left=Name(id='self', ctx=Load()),
                                ops=[Is()],
                                comparators=[Name(id='other', ctx=Load())],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__ne__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Compare(
                                left=Name(id='self', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Name(id='other', ctx=Load())],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__hash__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='object', ctx=Load()),
                                    attr='__hash__',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__call__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cr', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                            arg(arg='context', annotation=None, type_comment=None),
                            arg(arg='su', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return an environment based on ``self`` with modified parameters.\n\n            :param cr: optional database cursor to change the current cursor\n            :param user: optional user/user id to change the current user\n            :param context: optional context dictionary to change the current context\n            :param su: optional boolean to change the superuser mode\n            :type context: dict\n            :type user: int or :class:`~odoo.addons.base.models.res_users`\n            :type su: bool\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='cr', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='cr', ctx=Load()),
                                    ops=[Is()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='cr',
                                    ctx=Load(),
                                ),
                                orelse=Name(id='cr', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uid', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='user', ctx=Load()),
                                    ops=[Is()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='uid',
                                    ctx=Load(),
                                ),
                                orelse=Call(
                                    func=Name(id='int', ctx=Load()),
                                    args=[Name(id='user', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='context', ctx=Load()),
                                    ops=[Is()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='context',
                                    ctx=Load(),
                                ),
                                orelse=Name(id='context', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='su', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='su', ctx=Load()),
                                    ops=[Is()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=BoolOp(
                                    op=And(),
                                    values=[
                                        Compare(
                                            left=Name(id='user', ctx=Load()),
                                            ops=[Is()],
                                            comparators=[Constant(value=None, kind=None)],
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='su',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                orelse=Name(id='su', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='Environment', ctx=Load()),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='uid', ctx=Load()),
                                    Name(id='context', ctx=Load()),
                                    Name(id='su', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='ref',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='xml_id', annotation=None, type_comment=None),
                            arg(arg='raise_if_not_found', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Return the record corresponding to the given ``xml_id``.', kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='res_model', ctx=Store()),
                                        Name(id='res_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='self', ctx=Load()),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_xmlid_to_res_model_res_id',
                                    ctx=Load(),
                                ),
                                args=[Name(id='xml_id', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Name(id='raise_if_not_found', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='res_model', ctx=Load()),
                                    Name(id='res_id', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='record', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='self', ctx=Load()),
                                                slice=Name(id='res_model', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='res_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='record', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='raise_if_not_found', ctx=Load()),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValueError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='No record found for unique ID %s. It may have been deleted.', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='xml_id', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=None, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_superuser',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return whether the environment is in superuser mode. ', kind=None),
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='su',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_admin',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return whether the current user has group "Access Rights", or is in\n            superuser mode. ', kind=None),
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='su',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='_is_admin',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_system',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return whether the current user has group "Settings", or is in\n            superuser mode. ', kind=None),
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='su',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='_is_system',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='user',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Return the current user (as an instance).\n\n        :returns: current user - sudoed\n        :rtype: :class:`~odoo.addons.base.models.res_users`', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Call(
                                            func=Name(id='self', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='su',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='lazy_property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='company',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Return the current company (as an instance).\n\n        If not specified in the context (`allowed_company_ids`),\n        fallback on current user main company.\n\n        :raise AccessError: invalid or unauthorized `allowed_company_ids` context key content.\n        :return: current company (default=`self.user.company_id`), with the current environment\n        :rtype: res.company\n\n        .. warning::\n\n            No sanity checks applied in sudo mode !\n            When in sudo mode, a user can access any company,\n            even if not in his allowed companies.\n\n            This allows to trigger inter-company modifications,\n            even if the current user doesn't have access to\n            the targeted company.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='company_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='allowed_company_ids', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='company_ids', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='su',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='user_company_ids', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Name(id='cid', ctx=Load()),
                                                            ops=[NotIn()],
                                                            comparators=[Name(id='user_company_ids', ctx=Load())],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='cid', ctx=Store()),
                                                                iter=Name(id='company_ids', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='AccessError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Access to unauthorized or invalid companies.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='self', ctx=Load()),
                                                slice=Constant(value='res.company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='company_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='with_env',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='lazy_property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='companies',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Return a recordset of the enabled companies by the user.\n\n        If not specified in the context(`allowed_company_ids`),\n        fallback on current user companies.\n\n        :raise AccessError: invalid or unauthorized `allowed_company_ids` context key content.\n        :return: current companies (default=`self.user.company_ids`), with the current environment\n        :rtype: res.company\n\n        .. warning::\n\n            No sanity checks applied in sudo mode !\n            When in sudo mode, a user can access any company,\n            even if not in his allowed companies.\n\n            This allows to trigger inter-company modifications,\n            even if the current user doesn't have access to\n            the targeted company.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='company_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='allowed_company_ids', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='company_ids', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='su',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='user_company_ids', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Name(id='cid', ctx=Load()),
                                                            ops=[NotIn()],
                                                            comparators=[Name(id='user_company_ids', ctx=Load())],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='cid', ctx=Store()),
                                                                iter=Name(id='company_ids', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='AccessError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Access to unauthorized or invalid companies.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='self', ctx=Load()),
                                                slice=Constant(value='res.company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='company_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='company_ids',
                                        ctx=Load(),
                                    ),
                                    attr='with_env',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='lazy_property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='lang',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Return the current language code.\n\n        :rtype: str\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='lang', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='clear',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Clear all record caches, and discard all fields to recompute.\n            This may be useful when recovering from a failed ORM operation.\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='lazy_property', ctx=Load()),
                                    attr='reset_all',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='transaction',
                                        ctx=Load(),
                                    ),
                                    attr='clear',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='clear_upon_failure',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Context manager that rolls back the environments (caches and pending\n            computations and updates) upon exception.\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='warnings', ctx=Load()),
                                    attr='warn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Since Odoo 15.0, use cr.savepoint() instead of env.clear_upon_failure().', kind=None),
                                    Name(id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='stacklevel',
                                        value=Constant(value=2, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='savepoint',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_protected',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return whether `record` is protected against invalidation or\n            recomputation for `field`.\n        ', kind=None),
                        ),
                        Return(
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_protected',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='field', ctx=Load()),
                                            Tuple(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='protected',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the recordset for which ``field`` should not be invalidated or recomputed. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='self', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='model_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_protected',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='field', ctx=Load()),
                                            Tuple(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='protecting',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='what', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Prevent the invalidation or recomputation of fields on records.\n            The parameters are either:\n             - ``what`` a collection of fields and ``records`` a recordset, or\n             - ``what`` a collection of pairs ``(fields, records)``.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='protected', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_protected',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='protected', ctx=Load()),
                                            attr='pushmap',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='what', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='records', ctx=Load()),
                                            ops=[Is()],
                                            comparators=[Constant(value=None, kind=None)],
                                        ),
                                        body=Name(id='what', ctx=Load()),
                                        orelse=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='what', ctx=Load()),
                                                        Name(id='records', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='fields', ctx=Store()),
                                            Name(id='records', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Name(id='what', ctx=Load()),
                                    body=[
                                        For(
                                            target=Name(id='field', ctx=Store()),
                                            iter=Name(id='fields', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='ids', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='protected', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='field', ctx=Load()),
                                                            Call(
                                                                func=Name(id='frozenset', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='protected', ctx=Load()),
                                                            slice=Name(id='field', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ids', ctx=Load()),
                                                            attr='union',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='records', ctx=Load()),
                                                                attr='_ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Yield(value=None),
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='protected', ctx=Load()),
                                            attr='popmap',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[Name(id='contextmanager', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='fields_to_compute',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return a view on the field to compute. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='all',
                                            ctx=Load(),
                                        ),
                                        attr='tocompute',
                                        ctx=Load(),
                                    ),
                                    attr='keys',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='records_to_compute',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the records to compute for ``field``. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='all',
                                            ctx=Load(),
                                        ),
                                        attr='tocompute',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='field', ctx=Load()),
                                    Tuple(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='self', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='model_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='ids', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_to_compute',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return whether ``field`` must be computed on ``record``. ', kind=None),
                        ),
                        Return(
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='all',
                                                    ctx=Load(),
                                                ),
                                                attr='tocompute',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='field', ctx=Load()),
                                            Tuple(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='not_to_compute',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the subset of ``records`` for which ``field`` must not be computed. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='all',
                                            ctx=Load(),
                                        ),
                                        attr='tocompute',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='field', ctx=Load()),
                                    Tuple(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='records', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='id_', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='id_', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='records', ctx=Load()),
                                                    attr='_ids',
                                                    ctx=Load(),
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='id_', ctx=Load()),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='ids', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='add_to_compute',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Mark ``field`` to be computed on ``records``. ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='records', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='records', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='all',
                                                ctx=Load(),
                                            ),
                                            attr='tocompute',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='field', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='records', ctx=Load()),
                                        attr='_ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='remove_to_compute',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Mark ``field`` as computed on ``records``. ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='records', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='all',
                                            ctx=Load(),
                                        ),
                                        attr='tocompute',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='field', ctx=Load()),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='ids', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ids', ctx=Load()),
                                    attr='difference_update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='records', ctx=Load()),
                                        attr='_ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='ids', ctx=Load()),
                            ),
                            body=[
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='all',
                                                    ctx=Load(),
                                                ),
                                                attr='tocompute',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='field', ctx=Load()),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='norecompute',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Delay recomputations (deprecated: this is not the default behavior). ', kind=None),
                        ),
                        Expr(
                            value=Yield(value=None),
                        ),
                    ],
                    decorator_list=[Name(id='contextmanager', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='cache_key',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the cache key of the given ``field``. ', kind=None),
                        ),
                        Try(
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_cache_key',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='field', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='KeyError', ctx=Load()),
                                    name=None,
                                    body=[
                                        FunctionDef(
                                            name='get',
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[
                                                    arg(arg='key', annotation=None, type_comment=None),
                                                    arg(arg='get_context', annotation=None, type_comment=None),
                                                ],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='context',
                                                            ctx=Load(),
                                                        ),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='key', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='company', kind=None)],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='company',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='key', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='uid', kind=None)],
                                                            ),
                                                            body=[
                                                                Return(
                                                                    value=Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='uid',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='su',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='key', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='active_test', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Return(
                                                                            value=Call(
                                                                                func=Name(id='get_context', ctx=Load()),
                                                                                args=[
                                                                                    Constant(value='active_test', kind=None),
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='field', ctx=Load()),
                                                                                                attr='context',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='get',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Constant(value='active_test', kind=None),
                                                                                            Constant(value=True, kind=None),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Assign(
                                                                            targets=[Name(id='val', ctx=Store())],
                                                                            value=Call(
                                                                                func=Name(id='get_context', ctx=Load()),
                                                                                args=[Name(id='key', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        If(
                                                                            test=Compare(
                                                                                left=Call(
                                                                                    func=Name(id='type', ctx=Load()),
                                                                                    args=[Name(id='val', ctx=Load())],
                                                                                    keywords=[],
                                                                                ),
                                                                                ops=[Is()],
                                                                                comparators=[Name(id='list', ctx=Load())],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='val', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Name(id='tuple', ctx=Load()),
                                                                                        args=[Name(id='val', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                        Try(
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Name(id='hash', ctx=Load()),
                                                                                        args=[Name(id='val', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            handlers=[
                                                                                ExceptHandler(
                                                                                    type=Name(id='TypeError', ctx=Load()),
                                                                                    name=None,
                                                                                    body=[
                                                                                        Raise(
                                                                                            exc=Call(
                                                                                                func=Name(id='TypeError', ctx=Load()),
                                                                                                args=[
                                                                                                    Call(
                                                                                                        func=Attribute(
                                                                                                            value=Constant(value='Can only create cache keys from hashable values, got non-hashable value {!r} at context key {!r} (dependency of field {})', kind=None),
                                                                                                            attr='format',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[
                                                                                                            Name(id='val', ctx=Load()),
                                                                                                            Name(id='key', ctx=Load()),
                                                                                                            Name(id='field', ctx=Load()),
                                                                                                        ],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            cause=Constant(value=None, kind=None),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Return(
                                                                                    value=Name(id='val', ctx=Load()),
                                                                                ),
                                                                            ],
                                                                            finalbody=[],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            decorator_list=[],
                                            returns=None,
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='result', ctx=Store())],
                                            value=Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Call(
                                                            func=Name(id='get', ctx=Load()),
                                                            args=[Name(id='key', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='key', ctx=Store()),
                                                                iter=Subscript(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='registry',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='field_depends_context',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Name(id='field', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cache_key',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='field', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='result', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Name(id='result', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='Transaction',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' A object holding ORM data structures for a transaction. ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='registry', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='registry',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='registry', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='envs',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='WeakSet', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='cache',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='Cache', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='protected',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='StackMap', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='tocompute',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='set', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='towrite',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=Call(
                                            func=Name(id='defaultdict', ctx=Load()),
                                            args=[Name(id='dict', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='flush',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Flush pending computations and updates in the transaction. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='env_to_flush', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='env', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='envs',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='env', ctx=Load()),
                                                        attr='uid',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='int', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='env', ctx=Load()),
                                                    attr='uid',
                                                    ctx=Load(),
                                                ),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='env_to_flush', ctx=Store())],
                                            value=Name(id='env', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='env', ctx=Load()),
                                                    attr='uid',
                                                    ctx=Load(),
                                                ),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='env_to_flush', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env_to_flush', ctx=Load()),
                                                slice=Constant(value='base', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='clear',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Clear the caches and pending computations and updates in the translations. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='cache',
                                        ctx=Load(),
                                    ),
                                    attr='invalidate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tocompute',
                                        ctx=Load(),
                                    ),
                                    attr='clear',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='towrite',
                                        ctx=Load(),
                                    ),
                                    attr='clear',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='reset',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Reset the transaction.  This clears the transaction, and reassigns\n            the registry on all its environments.  This operation is strongly\n            recommended after reloading the registry.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='registry',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='Registry', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        attr='db_name',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='env', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='envs',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='env', ctx=Load()),
                                            attr='registry',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lazy_property', ctx=Load()),
                                            attr='reset_all',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='env', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='clear',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[Name(id='NOTHING', ctx=Store())],
            value=Call(
                func=Name(id='object', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='EMPTY_DICT', ctx=Store())],
            value=Call(
                func=Name(id='frozendict', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='Cache',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Implementation of the cache of records. ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_data',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='dict', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_field_cache',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the field cache of the given field, but not for modifying it. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field_cache', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_data',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='field', ctx=Load()),
                                    Name(id='EMPTY_DICT', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='field_cache', ctx=Load()),
                                    Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='model', ctx=Load()),
                                                attr='pool',
                                                ctx=Load(),
                                            ),
                                            attr='field_depends_context',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='field', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='field_cache', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='field_cache', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='model', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='cache_key',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='field', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Name(id='EMPTY_DICT', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='field_cache', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_field_cache',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the field cache of the given field for modifying it. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field_cache', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_data',
                                    ctx=Load(),
                                ),
                                slice=Name(id='field', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='pool',
                                        ctx=Load(),
                                    ),
                                    attr='field_depends_context',
                                    ctx=Load(),
                                ),
                                slice=Name(id='field', ctx=Load()),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='field_cache', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='field_cache', ctx=Load()),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='model', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='cache_key',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='field', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='field_cache', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='contains',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return whether ``record`` has a value for ``field``. ', kind=None),
                        ),
                        Return(
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_field_cache',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='record', ctx=Load()),
                                            Name(id='field', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Name(id='NOTHING', ctx=Load())],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the value of ``field`` for ``record``. ', kind=None),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='field_cache', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_field_cache',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='record', ctx=Load()),
                                            Name(id='field', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Subscript(
                                        value=Name(id='field_cache', ctx=Load()),
                                        slice=Subscript(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='KeyError', ctx=Load()),
                                    name=None,
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='default', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Name(id='NOTHING', ctx=Load())],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='CacheMiss', ctx=Load()),
                                                        args=[
                                                            Name(id='record', ctx=Load()),
                                                            Name(id='field', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Return(
                                            value=Name(id='default', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='set',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Set the value of ``field`` for ``record``. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field_cache', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_set_field_cache',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Name(id='field', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='field_cache', ctx=Load()),
                                    slice=Subscript(
                                        value=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='value', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='update',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Set the values of ``field`` for several ``records``. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field_cache', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_set_field_cache',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='records', ctx=Load()),
                                    Name(id='field', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='field_cache', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='zip', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='records', ctx=Load()),
                                                attr='_ids',
                                                ctx=Load(),
                                            ),
                                            Name(id='values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='remove',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Remove the value of ``field`` for ``record``. ', kind=None),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='field_cache', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_set_field_cache',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='record', ctx=Load()),
                                            Name(id='field', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='field_cache', ctx=Load()),
                                            slice=Subscript(
                                                value=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='KeyError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the cached values of ``field`` for ``records``. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field_cache', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_field_cache',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='records', ctx=Load()),
                                    Name(id='field', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record_id', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='records', ctx=Load()),
                                attr='_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Yield(
                                                value=Subscript(
                                                    value=Name(id='field_cache', ctx=Load()),
                                                    slice=Name(id='record_id', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='KeyError', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_until_miss',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the cached values of ``field`` for ``records`` until a value is not found. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field_cache', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_field_cache',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='records', ctx=Load()),
                                    Name(id='field', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record_id', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='records', ctx=Load()),
                                attr='_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='field_cache', ctx=Load()),
                                                        slice=Name(id='record_id', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='KeyError', ctx=Load()),
                                            name=None,
                                            body=[Break()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='vals', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_records_different_from',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the subset of ``records`` that has not ``value`` for ``field``. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field_cache', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_field_cache',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='records', ctx=Load()),
                                    Name(id='field', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record_id', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='records', ctx=Load()),
                                attr='_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='val', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='field_cache', ctx=Load()),
                                                slice=Name(id='record_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='KeyError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ids', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='record_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='val', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Name(id='value', ctx=Load())],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ids', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='record_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='records', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='ids', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the fields with a value for ``record``. ', kind=None),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='name', ctx=Store()),
                                    Name(id='field', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='_fields',
                                        ctx=Load(),
                                    ),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='name', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='id', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_field_cache',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='record', ctx=Load()),
                                                            Name(id='field', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Yield(
                                                value=Name(id='field', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_records',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the records of ``model`` that have a value for ``field``. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field_cache', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_field_cache',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='model', ctx=Load()),
                                    Name(id='field', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='field_cache', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_missing_ids',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the ids of ``records`` that have no value for ``field``. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field_cache', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_field_cache',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='records', ctx=Load()),
                                    Name(id='field', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record_id', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='records', ctx=Load()),
                                attr='_ids',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='record_id', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[Name(id='field_cache', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Yield(
                                                value=Name(id='record_id', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='invalidate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='spec', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Invalidate the cache, partially or totally depending on ``spec``. ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='spec', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_data',
                                                ctx=Load(),
                                            ),
                                            attr='clear',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='spec', ctx=Load()),
                                    body=[
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='field', ctx=Store()),
                                                    Name(id='ids', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Name(id='spec', ctx=Load()),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='ids', ctx=Load()),
                                                        ops=[Is()],
                                                        comparators=[Constant(value=None, kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_data',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='pop',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='field', ctx=Load()),
                                                                    Constant(value=None, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Continue(),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='cache', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_data',
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='field', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='cache', ctx=Load()),
                                                    ),
                                                    body=[Continue()],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='caches', ctx=Store())],
                                                    value=IfExp(
                                                        test=Call(
                                                            func=Name(id='isinstance', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Name(id='next', ctx=Load()),
                                                                    args=[
                                                                        Call(
                                                                            func=Name(id='iter', ctx=Load()),
                                                                            args=[Name(id='cache', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                Name(id='tuple', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        body=Call(
                                                            func=Attribute(
                                                                value=Name(id='cache', ctx=Load()),
                                                                attr='values',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        orelse=List(
                                                            elts=[Name(id='cache', ctx=Load())],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='field_cache', ctx=Store()),
                                                    iter=Name(id='caches', ctx=Load()),
                                                    body=[
                                                        For(
                                                            target=Name(id='id_', ctx=Store()),
                                                            iter=Name(id='ids', ctx=Load()),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='field_cache', ctx=Load()),
                                                                            attr='pop',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='id_', ctx=Load()),
                                                                            Constant(value=None, kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Check the consistency of the cache for the given environment. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='recompute',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dump', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_data',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='invalidate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='depends_context', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='env', ctx=Load()),
                                    attr='registry',
                                    ctx=Load(),
                                ),
                                attr='field_depends_context',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invalids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='check',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='model', annotation=None, type_comment=None),
                                    arg(arg='field', annotation=None, type_comment=None),
                                    arg(arg='field_dump', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='records', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='model_name',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='field_dump', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='records', ctx=Load()),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='cached', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='field_dump', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='value', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='field', ctx=Load()),
                                                            attr='convert_to_record',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='cached', ctx=Load()),
                                                            Name(id='record', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='fetched', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='record', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='field', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='fetched', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[Name(id='value', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='info', ctx=Store())],
                                                            value=Dict(
                                                                keys=[
                                                                    Constant(value='cached', kind=None),
                                                                    Constant(value='fetched', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='value', ctx=Load()),
                                                                    Name(id='fetched', ctx=Load()),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='invalids', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Name(id='record', ctx=Load()),
                                                                            Name(id='field', ctx=Load()),
                                                                            Name(id='info', ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Tuple(
                                                        elts=[
                                                            Name(id='AccessError', ctx=Load()),
                                                            Name(id='MissingError', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    name=None,
                                                    body=[Pass()],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='field', ctx=Store()),
                                    Name(id='field_dump', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='dump', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='model', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='model_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Subscript(
                                        value=Name(id='depends_context', ctx=Load()),
                                        slice=Name(id='field', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='context_keys', ctx=Store()),
                                                    Name(id='field_cache', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='field_dump', ctx=Load()),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='context', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='zip', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='depends_context', ctx=Load()),
                                                                        slice=Name(id='field', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='context_keys', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='check', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='model', ctx=Load()),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='context', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Name(id='field', ctx=Load()),
                                                            Name(id='field_cache', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='check', ctx=Load()),
                                                args=[
                                                    Name(id='model', ctx=Load()),
                                                    Name(id='field', ctx=Load()),
                                                    Name(id='field_dump', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='invalids', ctx=Load()),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Invalid cache for fields\n', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='pformat', ctx=Load()),
                                                    args=[Name(id='invalids', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='SUPERUSER_ID', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='AccessError', asname=None),
                alias(name='MissingError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.registry',
            names=[alias(name='Registry', asname=None)],
            level=0,
        ),
    ],
    type_ignores=[],
)
