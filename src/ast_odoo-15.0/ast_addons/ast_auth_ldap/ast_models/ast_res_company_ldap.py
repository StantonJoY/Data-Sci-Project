Module(
    body=[
        Import(
            names=[alias(name='ldap', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='ldap.filter',
            names=[alias(name='filter_format', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessDenied', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.pycompat',
            names=[alias(name='to_text', asname=None)],
            level=0,
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
        ClassDef(
            name='CompanyLDAP',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='res.company.ldap', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Company LDAP configuration', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='sequence', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='ldap_server', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=10, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ldap_server', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='LDAP Server address', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='127.0.0.1', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ldap_server_port', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='LDAP Server port', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=389, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ldap_binddn', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='LDAP binddn', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='The user account on the LDAP server that is used to query the directory. Leave empty to connect anonymously.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ldap_password', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='LDAP password', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The password of the user account on the LDAP server that is used to query the directory.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ldap_filter', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='LDAP filter', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='    Filter used to look up user accounts in the LDAP database. It is an    arbitrary LDAP filter in string representation. Any `%s` placeholder    will be replaced by the login (identifier) provided by the user, the filter    should contain at least one such placeholder.\n\n    The filter must result in exactly one (1) result, otherwise the login will    be considered invalid.\n\n    Example (actual attributes depend on LDAP server and setup):\n\n        (&(objectCategory=person)(objectClass=user)(sAMAccountName=%s))\n\n    or\n\n        (|(mail=%s)(uid=%s))\n    ', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ldap_base', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='LDAP base', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='DN of the user search scope: all descendants of this base will be searched for users.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.users', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Template User', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='User to copy when creating new users', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='create_user', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Automatically create local user accounts for new users authenticating via LDAP', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ldap_tls', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Use TLS', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Request secure TLS/SSL encryption when connecting to the LDAP server. This option requires a server with STARTTLS enabled, otherwise all authentication attempts will fail.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_ldap_dicts',
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
                            value=Constant(value='\n        Retrieve res_company_ldap resources from the database in dictionary\n        format.\n        :return: ldap configurations\n        :rtype: list of dictionaries\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ldaps', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='ldap_server', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='sequence', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ldaps', ctx=Load()),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='company', kind=None),
                                            Constant(value='ldap_server', kind=None),
                                            Constant(value='ldap_server_port', kind=None),
                                            Constant(value='ldap_binddn', kind=None),
                                            Constant(value='ldap_password', kind=None),
                                            Constant(value='ldap_filter', kind=None),
                                            Constant(value='ldap_base', kind=None),
                                            Constant(value='user', kind=None),
                                            Constant(value='create_user', kind=None),
                                            Constant(value='ldap_tls', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_connect',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='conf', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Connect to an LDAP server specified by an ldap\n        configuration dictionary.\n\n        :param dict conf: LDAP configuration\n        :return: an LDAP object\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='uri', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='ldap://%s:%d', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='conf', ctx=Load()),
                                            slice=Constant(value='ldap_server', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='conf', ctx=Load()),
                                            slice=Constant(value='ldap_server_port', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='connection', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ldap', ctx=Load()),
                                    attr='initialize',
                                    ctx=Load(),
                                ),
                                args=[Name(id='uri', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Subscript(
                                value=Name(id='conf', ctx=Load()),
                                slice=Constant(value='ldap_tls', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='connection', ctx=Load()),
                                            attr='start_tls_s',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='connection', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_entry',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='conf', annotation=None, type_comment=None),
                            arg(arg='login', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='filter_tmpl', ctx=Store())],
                            value=Subscript(
                                value=Name(id='conf', ctx=Load()),
                                slice=Constant(value='ldap_filter', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='placeholders', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='filter_tmpl', ctx=Load()),
                                    attr='count',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='%s', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='placeholders', ctx=Load()),
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
                                            Constant(value="LDAP filter %r contains no placeholder ('%%s').", kind=None),
                                            Name(id='filter_tmpl', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='formatted_filter', ctx=Store())],
                            value=Call(
                                func=Name(id='filter_format', ctx=Load()),
                                args=[
                                    Name(id='filter_tmpl', ctx=Load()),
                                    BinOp(
                                        left=List(
                                            elts=[Name(id='login', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Name(id='placeholders', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_query',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='conf', ctx=Load()),
                                    Name(id='formatted_filter', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='entry', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='entry', ctx=Store()),
                                        iter=Name(id='results', ctx=Load()),
                                        ifs=[
                                            Subscript(
                                                value=Name(id='entry', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='dn', ctx=Store()),
                                        Name(id='entry', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Constant(value=False, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='results', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='dn', ctx=Store()),
                                                Name(id='_', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        Name(id='entry', ctx=Store()),
                                    ],
                                    value=Subscript(
                                        value=Name(id='results', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='dn', ctx=Load()),
                                    Name(id='entry', ctx=Load()),
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
                    name='_authenticate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='conf', annotation=None, type_comment=None),
                            arg(arg='login', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Authenticate a user against the specified LDAP server.\n\n        In order to prevent an unintended 'unauthenticated authentication',\n        which is an anonymous bind with a valid dn and a blank password,\n        check for empty passwords explicitely (:rfc:`4513#section-6.3.1`)\n        :param dict conf: LDAP configuration\n        :param login: username\n        :param password: Password for the LDAP user\n        :return: LDAP entry of authenticated user or False\n        :rtype: dictionary of attributes\n        ", kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='password', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='dn', ctx=Store()),
                                        Name(id='entry', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_entry',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='conf', ctx=Load()),
                                    Name(id='login', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='dn', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='conn', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_connect',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='conf', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='conn', ctx=Load()),
                                            attr='simple_bind_s',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='dn', ctx=Load()),
                                            Call(
                                                func=Name(id='to_text', ctx=Load()),
                                                args=[Name(id='password', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='conn', ctx=Load()),
                                            attr='unbind',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='ldap', ctx=Load()),
                                        attr='INVALID_CREDENTIALS',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='ldap', ctx=Load()),
                                        attr='LDAPError',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='An LDAP exception occurred: %s', kind=None),
                                                    Name(id='e', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Name(id='entry', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_query',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='conf', annotation=None, type_comment=None),
                            arg(arg='filter', annotation=None, type_comment=None),
                            arg(arg='retrieve_attributes', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Query an LDAP server with the filter argument and scope subtree.\n\n        Allow for all authentication methods of the simple authentication\n        method:\n\n        - authenticated bind (non-empty binddn + valid password)\n        - anonymous bind (empty binddn + empty password)\n        - unauthenticated authentication (non-empty binddn + empty password)\n\n        .. seealso::\n           :rfc:`4513#section-5.1` - LDAP: Simple Authentication Method.\n\n        :param dict conf: LDAP configuration\n        :param filter: valid LDAP filter\n        :param list retrieve_attributes: LDAP attributes to be retrieved.         If not specified, return all attributes.\n        :return: ldap entries\n        :rtype: list of tuples (dn, attrs)\n\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='conn', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_connect',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='conf', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ldap_password', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Name(id='conf', ctx=Load()),
                                                slice=Constant(value='ldap_password', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ldap_binddn', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Name(id='conf', ctx=Load()),
                                                slice=Constant(value='ldap_binddn', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='conn', ctx=Load()),
                                            attr='simple_bind_s',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='to_text', ctx=Load()),
                                                args=[Name(id='ldap_binddn', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='to_text', ctx=Load()),
                                                args=[Name(id='ldap_password', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='results', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='conn', ctx=Load()),
                                            attr='search_st',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='to_text', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='conf', ctx=Load()),
                                                        slice=Constant(value='ldap_base', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='ldap', ctx=Load()),
                                                attr='SCOPE_SUBTREE',
                                                ctx=Load(),
                                            ),
                                            Name(id='filter', ctx=Load()),
                                            Name(id='retrieve_attributes', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='timeout',
                                                value=Constant(value=60, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='conn', ctx=Load()),
                                            attr='unbind',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='ldap', ctx=Load()),
                                        attr='INVALID_CREDENTIALS',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='LDAP bind failed.', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='ldap', ctx=Load()),
                                        attr='LDAPError',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='An LDAP exception occurred: %s', kind=None),
                                                    Name(id='e', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Name(id='results', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_map_ldap_attributes',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='conf', annotation=None, type_comment=None),
                            arg(arg='login', annotation=None, type_comment=None),
                            arg(arg='ldap_entry', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Compose values for a new resource of model res_users,\n        based upon the retrieved ldap entry and the LDAP settings.\n        :param dict conf: LDAP configuration\n        :param login: the new user's login\n        :param tuple ldap_entry: single LDAP result (dn, attrs)\n        :return: parameters for a new resource of model res_users\n        :rtype: dict\n        ", kind=None),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='login', kind=None),
                                    Constant(value='company_id', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='ustr',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='ldap_entry', ctx=Load()),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='cn', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='login', ctx=Load()),
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='conf', ctx=Load()),
                                            slice=Constant(value='company', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
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
                    name='_get_or_create_user',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='conf', annotation=None, type_comment=None),
                            arg(arg='login', annotation=None, type_comment=None),
                            arg(arg='ldap_entry', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Retrieve an active resource of model res_users with the specified\n        login. Create the user if it is not initially found.\n\n        :param dict conf: LDAP configuration\n        :param login: the user's login\n        :param tuple ldap_entry: single LDAP result (dn, attrs)\n        :return: res_users id\n        :rtype: int\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='login', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='ustr',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='login', ctx=Load()),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='SELECT id, active FROM res_users WHERE lower(login)=%s', kind=None),
                                    Tuple(
                                        elts=[Name(id='login', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchone',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='res', ctx=Load()),
                            body=[
                                If(
                                    test=Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Return(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Subscript(
                                        value=Name(id='conf', ctx=Load()),
                                        slice=Constant(value='create_user', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Creating new Odoo user "%s" from LDAP', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='login', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_map_ldap_attributes',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='conf', ctx=Load()),
                                                    Name(id='login', ctx=Load()),
                                                    Name(id='ldap_entry', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='SudoUser', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='res.users', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='no_reset_password',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Subscript(
                                                value=Name(id='conf', ctx=Load()),
                                                slice=Constant(value='user', kind=None),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='active', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                                Return(
                                                    value=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='SudoUser', ctx=Load()),
                                                                        attr='browse',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Subscript(
                                                                                value=Name(id='conf', ctx=Load()),
                                                                                slice=Constant(value='user', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='copy',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='default',
                                                                    value=Name(id='values', ctx=Load()),
                                                                ),
                                                            ],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Return(
                                                    value=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='SudoUser', ctx=Load()),
                                                                attr='create',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='values', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='AccessDenied', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='No local user found for LDAP login and not configured to create one', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_change_password',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='conf', annotation=None, type_comment=None),
                            arg(arg='login', annotation=None, type_comment=None),
                            arg(arg='old_passwd', annotation=None, type_comment=None),
                            arg(arg='new_passwd', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='changed', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='dn', ctx=Store()),
                                        Name(id='entry', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_entry',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='conf', ctx=Load()),
                                    Name(id='login', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='dn', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='conn', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_connect',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='conf', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='conn', ctx=Load()),
                                            attr='simple_bind_s',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='dn', ctx=Load()),
                                            Call(
                                                func=Name(id='to_text', ctx=Load()),
                                                args=[Name(id='old_passwd', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='conn', ctx=Load()),
                                            attr='passwd_s',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='dn', ctx=Load()),
                                            Name(id='old_passwd', ctx=Load()),
                                            Name(id='new_passwd', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='changed', ctx=Store())],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='conn', ctx=Load()),
                                            attr='unbind',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='ldap', ctx=Load()),
                                        attr='INVALID_CREDENTIALS',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[Pass()],
                                ),
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='ldap', ctx=Load()),
                                        attr='LDAPError',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='An LDAP exception occurred: %s', kind=None),
                                                    Name(id='e', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Name(id='changed', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
